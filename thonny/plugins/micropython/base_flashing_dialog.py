import os.path
import re
import tempfile
import threading
import traceback
import urllib.request
from abc import ABC, abstractmethod
from dataclasses import dataclass
from logging import getLogger
from tkinter import ttk
from typing import Any, Dict, List, Optional, Tuple

from thonny import get_runner
from thonny.languages import tr
from thonny.ui_utils import AdvancedLabel, MappingCombobox, set_text_if_different
from thonny.workdlg import WorkDialog

logger = getLogger(__name__)

FAKE_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"


@dataclass()
class TargetInfo:
    title: str
    path: str
    family: Optional[str]
    model: Optional[str]
    board_id: Optional[str]


class BaseFlashingDialog(WorkDialog, ABC):
    def __init__(self, master, firmware_name: str):
        self._downloaded_variants: List[Dict[str, Any]] = []

        self._last_handled_target = None
        self._last_handled_variant = None
        self.firmware_name = firmware_name

        threading.Thread(target=self._download_variants, daemon=True).start()

        super().__init__(master, autostart=False)

    @abstractmethod
    def get_variants_url(self) -> str:
        ...

    @abstractmethod
    def get_target_label(self) -> str:
        ...

    def populate_main_frame(self):
        epadx = self.get_large_padding()
        ipadx = self.get_small_padding()
        epady = epadx
        ipady = ipadx

        target_label = ttk.Label(self.main_frame, text=self.get_target_label())
        target_label.grid(row=1, column=1, sticky="e", padx=(epadx, 0), pady=(epady, 0))
        self._target_combo = MappingCombobox(self.main_frame, exportselection=False)
        self._target_combo.grid(
            row=1, column=2, sticky="nsew", padx=(ipadx, epadx), pady=(epady, 0)
        )

        self._target_info_label = ttk.Label(self.main_frame, text="model")
        self._target_info_label.grid(row=2, column=1, sticky="e", padx=(epadx, 0), pady=(ipady, 0))
        self._target_info_content_label = ttk.Label(self.main_frame)
        self._target_info_content_label.grid(
            row=2, column=2, sticky="w", padx=(ipadx, epadx), pady=(ipady, 0)
        )

        variant_label = ttk.Label(self.main_frame, text=f"{self.firmware_name} variant")
        variant_label.grid(row=5, column=1, sticky="e", padx=(epadx, 0), pady=(epady, 0))
        self._variant_combo = MappingCombobox(
            self.main_frame, exportselection=False, state="disabled"
        )
        self._variant_combo.grid(
            row=5, column=2, sticky="nsew", padx=(ipadx, epadx), pady=(epady, 0)
        )

        version_label = ttk.Label(self.main_frame, text="version")
        version_label.grid(row=6, column=1, sticky="e", padx=(epadx, 0), pady=(ipady, 0))
        self._version_combo = MappingCombobox(
            self.main_frame, exportselection=False, state="disabled"
        )
        self._version_combo.grid(
            row=6, column=2, sticky="nsew", padx=(ipadx, epadx), pady=(ipady, 0)
        )

        variant_info_label = ttk.Label(self.main_frame, text="info")
        variant_info_label.grid(row=7, column=1, sticky="e", padx=(epadx, 0), pady=(ipady, 0))
        self._variant_info_content_label = AdvancedLabel(self.main_frame)
        self._variant_info_content_label.grid(
            row=7, column=2, sticky="w", padx=(ipadx, epadx), pady=(ipady, 0)
        )

        self.main_frame.columnconfigure(2, weight=1)

    def update_ui(self):
        if self._state == "idle":
            targets = self.find_targets()
            if targets != self._target_combo.mapping:
                self.show_new_targets(targets)
                self._last_handled_target = None

            current_target = self._target_combo.get_selected_value()
            if not current_target:
                self._variant_combo.set_mapping({})
                self._variant_combo.select_none()
            elif current_target != self._last_handled_target and self._downloaded_variants:
                self._variant_combo.state(["!disabled", "readonly"])
                self._version_combo.state(["!disabled", "readonly"])
                self._present_variants_for_target(current_target)
                self._last_handled_target = current_target
                self._last_handled_variant = None
            self._update_target_info()

            current_variant = self._variant_combo.get_selected_value()
            if not current_variant:
                self._version_combo.select_none()
                self._version_combo.set_mapping({})
            elif current_variant != self._last_handled_variant:
                self._present_versions_for_variant(current_variant)
                self._last_handled_variant = current_variant
            self._update_variant_info()

        super().update_ui()

    @abstractmethod
    def find_targets(self) -> Dict[str, TargetInfo]:
        ...

    def show_new_targets(self, targets: Dict[str, TargetInfo]) -> None:
        self._target_combo.set_mapping(targets)
        if len(targets) == 1:
            self._target_combo.select_value(list(targets.values())[0])
        else:
            self._target_combo.select_none()

    @abstractmethod
    def compute_target_info_text_and_label(self, target: TargetInfo) -> Tuple[str, str]:
        ...

    def _update_target_info(self):
        current_target = self._target_combo.get_selected_value()
        if current_target is not None:
            text, label = self.compute_target_info_text_and_label(current_target)

        elif not self._target_combo.mapping:
            text = "[no suitable targets detected]"
            label = ""
        else:
            text = f"[found {len(self._target_combo.mapping)} targets, please select one]"
            label = ""

        set_text_if_different(self._target_info_content_label, text)
        set_text_if_different(self._target_info_label, label)

    def _update_variant_info(self):
        current_variant = self._variant_combo.get_selected_value()
        if not self._downloaded_variants:
            url = None
            text = "[downloading variants info ...]"
        elif current_variant:
            url = current_variant["info_url"]
            text = url
        elif self._variant_combo.mapping:
            url = None
            text = f"[select one from {len(self._variant_combo.mapping)} variants]"
        else:
            url = None
            text = ""

        set_text_if_different(self._variant_info_content_label, text)
        self._variant_info_content_label.set_url(url)

    def _present_variants_for_target(self, target: TargetInfo) -> None:
        assert self._downloaded_variants

        whole_mapping = {self._create_variant_description(v): v for v in self._downloaded_variants}

        if target.family is not None:
            filtered_mapping = {
                item[0]: item[1]
                for item in whole_mapping.items()
                if item[1]["family"].startswith(target.family)
            }
            if not filtered_mapping:
                filtered_mapping = whole_mapping
        else:
            filtered_mapping = whole_mapping

        prev_variant = self._variant_combo.get_selected_value()

        populars = {
            key: variant
            for key, variant in filtered_mapping.items()
            if variant.get("popular", False)
        }
        if populars and len(populars) < len(filtered_mapping):
            enhanced_mapping = {"--- MOST POPULAR " + "-" * 100: {}}
            for variant in populars.values():
                popular_variant = variant.copy()
                # need different title to distinguish it from the same item in ALL VARIANTS
                popular_title = self._create_variant_description(variant) + " "
                popular_variant["title"] = popular_title
                enhanced_mapping[popular_title] = popular_variant

            enhanced_mapping["--- ALL VARIANTS " + "-" * 100] = {}
            enhanced_mapping.update(filtered_mapping)
        else:
            enhanced_mapping = filtered_mapping

        self._variant_combo.set_mapping(enhanced_mapping)
        matches = list(
            filter(
                lambda v: self._variant_can_be_recommended_for_target(v, target),
                filtered_mapping.values(),
            )
        )

        if len(matches) == 1:
            self._variant_combo.select_value(matches[0])
        elif prev_variant and prev_variant in filtered_mapping.values():
            self._variant_combo.select_value(prev_variant)

    def _present_versions_for_variant(self, variant: Dict[str, Any]) -> None:
        versions_mapping = {d["version"]: d for d in variant["downloads"]}
        self._version_combo.set_mapping(versions_mapping)
        if len(versions_mapping) > 0:
            self._version_combo.select_value(list(versions_mapping.values())[0])
        else:
            self._version_combo.select_none()

    def _create_variant_description(self, variant: Dict[str, Any]) -> str:
        return variant["vendor"] + " • " + variant.get("title", variant["model"])

    @abstractmethod
    def _variant_can_be_recommended_for_target(self, variant: Dict[str, Any], target: TargetInfo):
        ...

    def _download_variants(self):
        logger.info("Downloading %r", self.get_variants_url())
        import json
        from urllib.request import urlopen

        try:
            req = urllib.request.Request(
                self.get_variants_url(),
                data=None,
                headers={
                    "User-Agent": FAKE_USER_AGENT,
                    "Cache-Control": "no-cache",
                },
            )
            with urlopen(req) as fp:
                json_str = fp.read().decode("UTF-8")
                # logger.debug("Variants info: %r", json_str)
            variants = json.loads(json_str)
            logger.info("Got %r variants", len(variants))
            self._tweak_variants(variants)
        except Exception:
            msg = f"Could not download variants info from {self.get_variants_url()}"
            logger.exception(msg)
            self.append_text(msg + "\n")
            self.set_action_text("Error!")
            self.grid_progress_widgets()
            return

        self._downloaded_variants = variants

    def _tweak_variants(self, variants):
        """
        A hack for getting the latest pre-release for micropython.org downloads.
        The build that is loaded from the json may already be deleted.
        In order to avoid adding another async operation into the process (after selecting
        a variant and before presenting versions), I'm getting the latest build substring
        from the download page of the first board and downloading it together with the json.
        """
        latest_prerelease_substitute = None
        latest_prerelease_regex: Optional[str] = None
        for variant in variants:
            new_regex = variant.get("latest_prerelease_regex", None)
            if new_regex:
                latest_prerelease_regex = new_regex
                import json
                import urllib.request

                logger.info("Downloading %r", variant["info_url"])
                try:
                    req = urllib.request.Request(
                        variant["info_url"],
                        data=None,
                        headers={
                            "User-Agent": FAKE_USER_AGENT,
                            "Cache-Control": "no-cache",
                        },
                    )
                    with urllib.request.urlopen(req) as fp:
                        html_str = fp.read().decode("UTF-8", errors="replace")
                        # logger.debug("Variants info: %r", json_str)

                    match = re.search(latest_prerelease_regex, html_str)
                    if match:
                        latest_prerelease_substitute = match.group(0)
                        logger.info(
                            "Using %r as prerelease substitute", latest_prerelease_substitute
                        )
                    else:
                        latest_prerelease_substitute = None
                except Exception:
                    msg = f"Could not download variants info from {self.get_variants_url()}"
                    logger.exception(msg)
                    self.append_text(msg + "\n")
                    self.set_action_text("Error!")
                    self.grid_progress_widgets()

            if latest_prerelease_substitute:
                assert latest_prerelease_regex
                for i, download in enumerate(variant["downloads"]):
                    patched_url = re.sub(
                        latest_prerelease_regex, latest_prerelease_substitute, download["url"]
                    )
                    if patched_url != download["url"]:
                        logger.debug("Replacing %r with %r", download["url"], patched_url)
                        download["url"] = patched_url
                        download["version"] = latest_prerelease_substitute

    def get_ok_text(self):
        return tr("Install")

    def _on_variant_select(self, *args):
        pass

    def is_ready_for_work(self):
        return self._target_combo.get_selected_value() and self._version_combo.get_selected_value()

    def start_work(self):
        from thonny.plugins.micropython import BareMetalMicroPythonProxy

        variant_info: Dict[str, Any] = self._variant_combo.get_selected_value()
        download_info: Dict[str, Any] = self._version_combo.get_selected_value()
        assert download_info
        target_info: TargetInfo = self._target_combo.get_selected_value()
        assert target_info

        self.report_progress(0, 100)
        proxy = get_runner().get_backend_proxy()
        if isinstance(proxy, BareMetalMicroPythonProxy):
            proxy.disconnect()

        threading.Thread(
            target=self._perform_work_and_update_status,
            args=[
                variant_info,
                download_info,
                target_info,
            ],
            daemon=True,
        ).start()
        return True

    def _perform_work_and_update_status(
        self, variant_info: Dict[str, Any], download_info: Dict[str, str], target_info: TargetInfo
    ) -> None:
        try:
            temp_file = self._download_to_temp(download_info)

            self.upload_to_device(temp_file, variant_info, download_info, target_info)
        except Exception as e:
            self.append_text("\n" + "".join(traceback.format_exc()))
            self.set_action_text("Error...")
            self.report_done(False)
            return

        if self._state == "working":
            self.append_text("\nDone!\n")
            self.set_action_text("Done!")
            self.report_done(True)
        else:
            assert self._state == "cancelling"
            self.append_text("\nCancelled\n")
            self.set_action_text("Cancelled")
            self.report_done(False)

    def _download_to_temp(self, download_info: Dict[str, str]) -> str:
        """Running in a bg thread"""
        from urllib.request import urlopen

        target_dir = tempfile.mkdtemp()
        target_filename = download_info.get("filename", download_info["url"].split("/")[-1])
        download_url = download_info["url"]
        size = download_info.get("size", None)

        target_path = os.path.join(target_dir, target_filename)
        logger.debug("Downloading from %s", download_url)

        self.set_action_text("Starting...")
        self.append_text("Downloading from %s\n" % download_url)

        req = urllib.request.Request(
            download_url,
            data=None,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
            },
        )

        with urlopen(req, timeout=5) as fsrc:
            if size is None:
                size = int(fsrc.getheader("Content-Length", str(500 * 1024)))

            bytes_copied = 0
            self.append_text("Writing to %s\n" % target_path)
            self.append_text("Starting...")
            if fsrc.length:
                # override (possibly inaccurate) size
                size = fsrc.length

            block_size = 8 * 1024
            with open(target_path, "wb") as fdst:
                while True:
                    block = fsrc.read(block_size)
                    if not block:
                        break

                    if self._state == "cancelling":
                        break

                    fdst.write(block)
                    bytes_copied += len(block)
                    percent_done = bytes_copied / size * 100
                    percent_str = "%.0f%%" % (percent_done)
                    self.set_action_text("Downloading... " + percent_str)

                    # leaving left half of the progressbar for downloading
                    self.report_progress(percent_done, 200)
                    self.replace_last_line(percent_str)

        return target_path

    @abstractmethod
    def upload_to_device(
        self,
        source_path: str,
        variant_info: Dict[str, Any],
        download_info: Dict[str, str],
        target_info: TargetInfo,
    ) -> None:
        ...


def find_uf2_property(lines: List[str], prop_name: str) -> Optional[str]:
    marker = prop_name + ": "
    for line in lines:
        if line.startswith(marker):
            return line[len(marker) :]

    return None