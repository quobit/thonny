# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: exa/codeium_common_pb/codeium_common.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'exa/codeium_common_pb/codeium_common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*exa/codeium_common_pb/codeium_common.proto\x12\x15\x65xa.codeium_common_pb\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xce\x02\n\nCompletion\x12#\n\rcompletion_id\x18\x01 \x01(\tR\x0c\x63ompletionId\x12\x12\n\x04text\x18\x02 \x01(\tR\x04text\x12\x16\n\x06prefix\x18\x03 \x01(\tR\x06prefix\x12\x12\n\x04stop\x18\x04 \x01(\tR\x04stop\x12\x14\n\x05score\x18\x05 \x01(\x01R\x05score\x12\x16\n\x06tokens\x18\x06 \x03(\x04R\x06tokens\x12%\n\x0e\x64\x65\x63oded_tokens\x18\x07 \x03(\tR\rdecodedTokens\x12$\n\rprobabilities\x18\x08 \x03(\x01R\rprobabilities\x12\x35\n\x16\x61\x64justed_probabilities\x18\t \x03(\x01R\x15\x61\x64justedProbabilities\x12)\n\x10generated_length\x18\n \x01(\x04R\x0fgeneratedLength\"\x89\x02\n\x08Metadata\x12\x19\n\x08ide_name\x18\x01 \x01(\tR\x07ideName\x12\x1f\n\x0bide_version\x18\x07 \x01(\tR\nideVersion\x12%\n\x0e\x65xtension_name\x18\x0c \x01(\tR\rextensionName\x12+\n\x11\x65xtension_version\x18\x02 \x01(\tR\x10\x65xtensionVersion\x12\x17\n\x07\x61pi_key\x18\x03 \x01(\tR\x06\x61piKey\x12\x16\n\x06locale\x18\x04 \x01(\tR\x06locale\x12\x1d\n\nsession_id\x18\n \x01(\tR\tsessionId\x12\x1d\n\nrequest_id\x18\t \x01(\x04R\trequestId\"\x93\x01\n\x05\x45vent\x12?\n\nevent_type\x18\x01 \x01(\x0e\x32 .exa.codeium_common_pb.EventTypeR\teventType\x12\x1d\n\nevent_json\x18\x02 \x01(\tR\teventJson\x12*\n\x11timestamp_unix_ms\x18\x03 \x01(\x03R\x0ftimestampUnixMs\"\xac\x03\n\x0c\x46unctionInfo\x12\x1d\n\nraw_source\x18\x01 \x01(\tR\trawSource\x12%\n\x0e\x63lean_function\x18\x02 \x01(\tR\rcleanFunction\x12\x1c\n\tdocstring\x18\x03 \x01(\tR\tdocstring\x12\x1b\n\tnode_name\x18\x04 \x01(\tR\x08nodeName\x12\x16\n\x06params\x18\x05 \x01(\tR\x06params\x12\'\n\x0f\x64\x65\x66inition_line\x18\x06 \x01(\x05R\x0e\x64\x65\x66initionLine\x12\x1d\n\nstart_line\x18\x07 \x01(\x05R\tstartLine\x12\x19\n\x08\x65nd_line\x18\x08 \x01(\x05R\x07\x65ndLine\x12\x1b\n\tstart_col\x18\t \x01(\x05R\x08startCol\x12\x17\n\x07\x65nd_col\x18\n \x01(\x05R\x06\x65ndCol\x12-\n\x12leading_whitespace\x18\x0b \x01(\tR\x11leadingWhitespace\x12;\n\x08language\x18\x0c \x01(\x0e\x32\x1f.exa.codeium_common_pb.LanguageR\x08language\"\xb9\x05\n\x0f\x43odeContextItem\x12#\n\rabsolute_path\x18\x01 \x01(\tR\x0c\x61\x62solutePath\x12M\n\x0fworkspace_paths\x18\x02 \x03(\x0b\x32$.exa.codeium_common_pb.WorkspacePathR\x0eworkspacePaths\x12\x1b\n\tnode_name\x18\x03 \x01(\tR\x08nodeName\x12!\n\x0cnode_lineage\x18\x04 \x03(\tR\x0bnodeLineage\x12\x1d\n\nstart_line\x18\x05 \x01(\rR\tstartLine\x12\x1b\n\tstart_col\x18\x0c \x01(\rR\x08startCol\x12\x19\n\x08\x65nd_line\x18\x06 \x01(\rR\x07\x65ndLine\x12\x17\n\x07\x65nd_col\x18\r \x01(\rR\x06\x65ndCol\x12I\n\x0c\x63ontext_type\x18\x07 \x01(\x0e\x32&.exa.codeium_common_pb.CodeContextTypeR\x0b\x63ontextType\x12;\n\x08language\x18\n \x01(\x0e\x32\x1f.exa.codeium_common_pb.LanguageR\x08language\x12\x61\n\x0fsnippet_by_type\x18\x0b \x03(\x0b\x32\x39.exa.codeium_common_pb.CodeContextItem.SnippetByTypeEntryR\rsnippetByType\x1am\n\x12SnippetByTypeEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32+.exa.codeium_common_pb.SnippetWithWordCountR\x05value:\x02\x38\x01J\x04\x08\x08\x10\tJ\x04\x08\t\x10\nR\x0c\x63ode_snippetR\x0e\x63ode_signature\"\x95\x02\n\x14SnippetWithWordCount\x12\x18\n\x07snippet\x18\x01 \x01(\tR\x07snippet\x12y\n\x16word_count_by_splitter\x18\x02 \x03(\x0b\x32\x44.exa.codeium_common_pb.SnippetWithWordCount.WordCountBySplitterEntryR\x13wordCountBySplitter\x1ah\n\x18WordCountBySplitterEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32 .exa.codeium_common_pb.WordCountR\x05value:\x02\x38\x01\"\xa6\x01\n\tWordCount\x12X\n\x0eword_count_map\x18\x01 \x03(\x0b\x32\x32.exa.codeium_common_pb.WordCount.WordCountMapEntryR\x0cwordCountMap\x1a?\n\x11WordCountMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"R\n\rWorkspacePath\x12\x1c\n\tworkspace\x18\x01 \x01(\tR\tworkspace\x12#\n\rrelative_path\x18\x02 \x01(\tR\x0crelativePath\"\x83\x02\n\nUserStatus\x12\x10\n\x03pro\x18\x01 \x01(\x08R\x03pro\x12+\n\x11\x64isable_telemetry\x18\x02 \x01(\x08R\x10\x64isableTelemetry\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x41\n\x1dignore_chat_telemetry_setting\x18\x04 \x01(\x08R\x1aignoreChatTelemetrySetting\x12\x17\n\x07team_id\x18\x05 \x01(\tR\x06teamId\x12\x46\n\x0bteam_status\x18\x06 \x01(\x0e\x32%.exa.codeium_common_pb.UserTeamStatusR\nteamStatus\"\xab\x01\n\x11\x45mbeddingMetadata\x12\x1b\n\tnode_name\x18\x01 \x01(\tR\x08nodeName\x12\x1d\n\nstart_line\x18\x02 \x01(\rR\tstartLine\x12\x19\n\x08\x65nd_line\x18\x03 \x01(\rR\x07\x65ndLine\x12?\n\nembed_type\x18\x04 \x01(\x0e\x32 .exa.codeium_common_pb.EmbedTypeR\tembedType\"\xa8\x01\n\x0cUserSettings\x12J\n\"open_most_recent_chat_conversation\x18\x01 \x01(\x08R\x1eopenMostRecentChatConversation\x12L\n\x13last_selected_model\x18\x02 \x01(\x0e\x32\x1c.exa.codeium_common_pb.ModelR\x11lastSelectedModel\"\xfa\x01\n\x0bGitRepoInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05owner\x18\x02 \x01(\tR\x05owner\x12\x1b\n\trepo_name\x18\x05 \x01(\tR\x08repoName\x12\x16\n\x06\x63ommit\x18\x03 \x01(\tR\x06\x63ommit\x12#\n\rversion_alias\x18\x04 \x01(\tR\x0cversionAlias\x12\x45\n\x0cscm_provider\x18\x06 \x01(\x0e\x32\".exa.codeium_common_pb.ScmProviderR\x0bscmProvider\x12 \n\x0c\x62\x61se_git_url\x18\x07 \x01(\tR\nbaseGitUrl\"\x98\x01\n\rEditorOptions\x12\x19\n\x08tab_size\x18\x01 \x01(\x04R\x07tabSize\x12#\n\rinsert_spaces\x18\x02 \x01(\x08R\x0cinsertSpaces\x12G\n disable_autocomplete_in_comments\x18\x03 \x01(\x08R\x1d\x64isableAutocompleteInComments*\xb4\x01\n\tEventType\x12\x1a\n\x16\x45VENT_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x45VENT_TYPE_ENABLE_CODEIUM\x10\x01\x12\x1e\n\x1a\x45VENT_TYPE_DISABLE_CODEIUM\x10\x02\x12\'\n#EVENT_TYPE_SHOW_PREVIOUS_COMPLETION\x10\x03\x12#\n\x1f\x45VENT_TYPE_SHOW_NEXT_COMPLETION\x10\x04*\x9c\x01\n\x10\x43ompletionSource\x12!\n\x1d\x43OMPLETION_SOURCE_UNSPECIFIED\x10\x00\x12)\n%COMPLETION_SOURCE_TYPING_AS_SUGGESTED\x10\x01\x12\x1b\n\x17\x43OMPLETION_SOURCE_CACHE\x10\x02\x12\x1d\n\x19\x43OMPLETION_SOURCE_NETWORK\x10\x03*\x92\x0f\n\x08Language\x12\x18\n\x14LANGUAGE_UNSPECIFIED\x10\x00\x12\x0e\n\nLANGUAGE_C\x10\x01\x12\x14\n\x10LANGUAGE_CLOJURE\x10\x02\x12\x19\n\x15LANGUAGE_COFFEESCRIPT\x10\x03\x12\x10\n\x0cLANGUAGE_CPP\x10\x04\x12\x13\n\x0fLANGUAGE_CSHARP\x10\x05\x12\x10\n\x0cLANGUAGE_CSS\x10\x06\x12\x14\n\x10LANGUAGE_CUDACPP\x10\x07\x12\x17\n\x13LANGUAGE_DOCKERFILE\x10\x08\x12\x0f\n\x0bLANGUAGE_GO\x10\t\x12\x13\n\x0fLANGUAGE_GROOVY\x10\n\x12\x17\n\x13LANGUAGE_HANDLEBARS\x10\x0b\x12\x14\n\x10LANGUAGE_HASKELL\x10\x0c\x12\x10\n\x0cLANGUAGE_HCL\x10\r\x12\x11\n\rLANGUAGE_HTML\x10\x0e\x12\x10\n\x0cLANGUAGE_INI\x10\x0f\x12\x11\n\rLANGUAGE_JAVA\x10\x10\x12\x17\n\x13LANGUAGE_JAVASCRIPT\x10\x11\x12\x11\n\rLANGUAGE_JSON\x10\x12\x12\x12\n\x0eLANGUAGE_JULIA\x10\x13\x12\x13\n\x0fLANGUAGE_KOTLIN\x10\x14\x12\x12\n\x0eLANGUAGE_LATEX\x10\x15\x12\x11\n\rLANGUAGE_LESS\x10\x16\x12\x10\n\x0cLANGUAGE_LUA\x10\x17\x12\x15\n\x11LANGUAGE_MAKEFILE\x10\x18\x12\x15\n\x11LANGUAGE_MARKDOWN\x10\x19\x12\x17\n\x13LANGUAGE_OBJECTIVEC\x10\x1a\x12\x19\n\x15LANGUAGE_OBJECTIVECPP\x10\x1b\x12\x11\n\rLANGUAGE_PERL\x10\x1c\x12\x10\n\x0cLANGUAGE_PHP\x10\x1d\x12\x16\n\x12LANGUAGE_PLAINTEXT\x10\x1e\x12\x15\n\x11LANGUAGE_PROTOBUF\x10\x1f\x12\x12\n\x0eLANGUAGE_PBTXT\x10 \x12\x13\n\x0fLANGUAGE_PYTHON\x10!\x12\x0e\n\nLANGUAGE_R\x10\"\x12\x11\n\rLANGUAGE_RUBY\x10#\x12\x11\n\rLANGUAGE_RUST\x10$\x12\x11\n\rLANGUAGE_SASS\x10%\x12\x12\n\x0eLANGUAGE_SCALA\x10&\x12\x11\n\rLANGUAGE_SCSS\x10\'\x12\x12\n\x0eLANGUAGE_SHELL\x10(\x12\x10\n\x0cLANGUAGE_SQL\x10)\x12\x15\n\x11LANGUAGE_STARLARK\x10*\x12\x12\n\x0eLANGUAGE_SWIFT\x10+\x12\x10\n\x0cLANGUAGE_TSX\x10,\x12\x17\n\x13LANGUAGE_TYPESCRIPT\x10-\x12\x18\n\x14LANGUAGE_VISUALBASIC\x10.\x12\x10\n\x0cLANGUAGE_VUE\x10/\x12\x10\n\x0cLANGUAGE_XML\x10\x30\x12\x10\n\x0cLANGUAGE_XSL\x10\x31\x12\x11\n\rLANGUAGE_YAML\x10\x32\x12\x13\n\x0fLANGUAGE_SVELTE\x10\x33\x12\x11\n\rLANGUAGE_TOML\x10\x34\x12\x11\n\rLANGUAGE_DART\x10\x35\x12\x10\n\x0cLANGUAGE_RST\x10\x36\x12\x12\n\x0eLANGUAGE_OCAML\x10\x37\x12\x12\n\x0eLANGUAGE_CMAKE\x10\x38\x12\x13\n\x0fLANGUAGE_PASCAL\x10\x39\x12\x13\n\x0fLANGUAGE_ELIXIR\x10:\x12\x13\n\x0fLANGUAGE_FSHARP\x10;\x12\x11\n\rLANGUAGE_LISP\x10<\x12\x13\n\x0fLANGUAGE_MATLAB\x10=\x12\x17\n\x13LANGUAGE_POWERSHELL\x10>\x12\x15\n\x11LANGUAGE_SOLIDITY\x10?\x12\x10\n\x0cLANGUAGE_ADA\x10@\x12\x1c\n\x18LANGUAGE_OCAML_INTERFACE\x10\x41\x12\x1e\n\x1aLANGUAGE_TREE_SITTER_QUERY\x10\x42\x12\x10\n\x0cLANGUAGE_APL\x10\x43\x12\x15\n\x11LANGUAGE_ASSEMBLY\x10\x44\x12\x12\n\x0eLANGUAGE_COBOL\x10\x45\x12\x14\n\x10LANGUAGE_CRYSTAL\x10\x46\x12\x17\n\x13LANGUAGE_EMACS_LISP\x10G\x12\x13\n\x0fLANGUAGE_ERLANG\x10H\x12\x14\n\x10LANGUAGE_FORTRAN\x10I\x12\x15\n\x11LANGUAGE_FREEFORM\x10J\x12\x13\n\x0fLANGUAGE_GRADLE\x10K\x12\x11\n\rLANGUAGE_HACK\x10L\x12\x12\n\x0eLANGUAGE_MAVEN\x10M\x12\x19\n\x15LANGUAGE_M68KASSEMBLY\x10N\x12\x10\n\x0cLANGUAGE_SAS\x10O\x12\x19\n\x15LANGUAGE_UNIXASSEMBLY\x10P\x12\x10\n\x0cLANGUAGE_VBA\x10Q\x12\x16\n\x12LANGUAGE_VIMSCRIPT\x10R\x12\x18\n\x14LANGUAGE_WEBASSEMBLY\x10S\x12\x12\n\x0eLANGUAGE_BLADE\x10T\x12\x12\n\x0eLANGUAGE_ASTRO\x10U\x12\x12\n\x0eLANGUAGE_MUMPS\x10V\x12\x15\n\x11LANGUAGE_GDSCRIPT\x10W\x12\x10\n\x0cLANGUAGE_NIM\x10X\x12\x13\n\x0fLANGUAGE_PROLOG\x10Y\x12\x1c\n\x18LANGUAGE_MARKDOWN_INLINE\x10Z*\x97\x01\n\x11\x43hatMessageSource\x12#\n\x1f\x43HAT_MESSAGE_SOURCE_UNSPECIFIED\x10\x00\x12\x1c\n\x18\x43HAT_MESSAGE_SOURCE_USER\x10\x01\x12\x1e\n\x1a\x43HAT_MESSAGE_SOURCE_SYSTEM\x10\x02\x12\x1f\n\x1b\x43HAT_MESSAGE_SOURCE_UNKNOWN\x10\x03*\xa3\x02\n\x0f\x43odeContextType\x12!\n\x1d\x43ODE_CONTEXT_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1a\x43ODE_CONTEXT_TYPE_FUNCTION\x10\x01\x12\x1b\n\x17\x43ODE_CONTEXT_TYPE_CLASS\x10\x02\x12\x1c\n\x18\x43ODE_CONTEXT_TYPE_IMPORT\x10\x03\x12%\n!CODE_CONTEXT_TYPE_NAIVE_LINECHUNK\x10\x04\x12(\n$CODE_CONTEXT_TYPE_REFERENCE_FUNCTION\x10\x05\x12%\n!CODE_CONTEXT_TYPE_REFERENCE_CLASS\x10\x06\x12\x1a\n\x16\x43ODE_CONTEXT_TYPE_FILE\x10\x07*\xa6\x01\n\x12\x43ontextSnippetType\x12$\n CONTEXT_SNIPPET_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1f\x43ONTEXT_SNIPPET_TYPE_RAW_SOURCE\x10\x01\x12\"\n\x1e\x43ONTEXT_SNIPPET_TYPE_SIGNATURE\x10\x02\x12!\n\x1d\x43ONTEXT_SNIPPET_TYPE_NODEPATH\x10\x03*\x86\x01\n\x14\x43ontextInclusionType\x12&\n\"CONTEXT_INCLUSION_TYPE_UNSPECIFIED\x10\x00\x12\"\n\x1e\x43ONTEXT_INCLUSION_TYPE_INCLUDE\x10\x01\x12\"\n\x1e\x43ONTEXT_INCLUSION_TYPE_EXCLUDE\x10\x02* \n\rExperimentKey\x12\x0f\n\x0bUNSPECIFIED\x10\x00*\x8e\x01\n\x0eUserTeamStatus\x12 \n\x1cUSER_TEAM_STATUS_UNSPECIFIED\x10\x00\x12\x1c\n\x18USER_TEAM_STATUS_PENDING\x10\x01\x12\x1d\n\x19USER_TEAM_STATUS_APPROVED\x10\x02\x12\x1d\n\x19USER_TEAM_STATUS_REJECTED\x10\x03*\xe0\x01\n\tEmbedType\x12\x1a\n\x16\x45MBED_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x45MBED_TYPE_RAW_SOURCE\x10\x01\x12\x18\n\x14\x45MBED_TYPE_DOCSTRING\x10\x02\x12\x17\n\x13\x45MBED_TYPE_FUNCTION\x10\x03\x12\x17\n\x13\x45MBED_TYPE_NODEPATH\x10\x04\x12\x1a\n\x16\x45MBED_TYPE_DECLARATION\x10\x05\x12\x1a\n\x16\x45MBED_TYPE_NAIVE_CHUNK\x10\x06\x12\x18\n\x14\x45MBED_TYPE_SIGNATURE\x10\x07*y\n\x0bScmProvider\x12\x1c\n\x18SCM_PROVIDER_UNSPECIFIED\x10\x00\x12\x17\n\x13SCM_PROVIDER_GITHUB\x10\x01\x12\x17\n\x13SCM_PROVIDER_GITLAB\x10\x02\x12\x1a\n\x16SCM_PROVIDER_BITBUCKET\x10\x03*\x94\x01\n\x05Model\x12\x15\n\x11MODEL_UNSPECIFIED\x10\x00\x12\x18\n\x14MODEL_CHAT_3_5_TURBO\x10\x1c\x12!\n\x1dMODEL_CHAT_GPT_3_5_TURBO_1106\x10$\x12\x14\n\x10MODEL_CHAT_GPT_4\x10\x1e\x12!\n\x1dMODEL_CHAT_GPT_4_1106_PREVIEW\x10%B\xd6\x01\n\x19\x63om.exa.codeium_common_pbB\x12\x43odeiumCommonProtoP\x01Z8github.com/Exafunction/Exafunction/exa/codeium_common_pb\xa2\x02\x03\x45\x43X\xaa\x02\x13\x45xa.CodeiumCommonPb\xca\x02\x13\x45xa\\CodeiumCommonPb\xe2\x02\x1f\x45xa\\CodeiumCommonPb\\GPBMetadata\xea\x02\x14\x45xa::CodeiumCommonPbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exa.codeium_common_pb.codeium_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.exa.codeium_common_pbB\022CodeiumCommonProtoP\001Z8github.com/Exafunction/Exafunction/exa/codeium_common_pb\242\002\003ECX\252\002\023Exa.CodeiumCommonPb\312\002\023Exa\\CodeiumCommonPb\342\002\037Exa\\CodeiumCommonPb\\GPBMetadata\352\002\024Exa::CodeiumCommonPb'
  _globals['_CODECONTEXTITEM_SNIPPETBYTYPEENTRY']._loaded_options = None
  _globals['_CODECONTEXTITEM_SNIPPETBYTYPEENTRY']._serialized_options = b'8\001'
  _globals['_SNIPPETWITHWORDCOUNT_WORDCOUNTBYSPLITTERENTRY']._loaded_options = None
  _globals['_SNIPPETWITHWORDCOUNT_WORDCOUNTBYSPLITTERENTRY']._serialized_options = b'8\001'
  _globals['_WORDCOUNT_WORDCOUNTMAPENTRY']._loaded_options = None
  _globals['_WORDCOUNT_WORDCOUNTMAPENTRY']._serialized_options = b'8\001'
  _globals['_EVENTTYPE']._serialized_start=3569
  _globals['_EVENTTYPE']._serialized_end=3749
  _globals['_COMPLETIONSOURCE']._serialized_start=3752
  _globals['_COMPLETIONSOURCE']._serialized_end=3908
  _globals['_LANGUAGE']._serialized_start=3911
  _globals['_LANGUAGE']._serialized_end=5849
  _globals['_CHATMESSAGESOURCE']._serialized_start=5852
  _globals['_CHATMESSAGESOURCE']._serialized_end=6003
  _globals['_CODECONTEXTTYPE']._serialized_start=6006
  _globals['_CODECONTEXTTYPE']._serialized_end=6297
  _globals['_CONTEXTSNIPPETTYPE']._serialized_start=6300
  _globals['_CONTEXTSNIPPETTYPE']._serialized_end=6466
  _globals['_CONTEXTINCLUSIONTYPE']._serialized_start=6469
  _globals['_CONTEXTINCLUSIONTYPE']._serialized_end=6603
  _globals['_EXPERIMENTKEY']._serialized_start=6605
  _globals['_EXPERIMENTKEY']._serialized_end=6637
  _globals['_USERTEAMSTATUS']._serialized_start=6640
  _globals['_USERTEAMSTATUS']._serialized_end=6782
  _globals['_EMBEDTYPE']._serialized_start=6785
  _globals['_EMBEDTYPE']._serialized_end=7009
  _globals['_SCMPROVIDER']._serialized_start=7011
  _globals['_SCMPROVIDER']._serialized_end=7132
  _globals['_MODEL']._serialized_start=7135
  _globals['_MODEL']._serialized_end=7283
  _globals['_COMPLETION']._serialized_start=135
  _globals['_COMPLETION']._serialized_end=469
  _globals['_METADATA']._serialized_start=472
  _globals['_METADATA']._serialized_end=737
  _globals['_EVENT']._serialized_start=740
  _globals['_EVENT']._serialized_end=887
  _globals['_FUNCTIONINFO']._serialized_start=890
  _globals['_FUNCTIONINFO']._serialized_end=1318
  _globals['_CODECONTEXTITEM']._serialized_start=1321
  _globals['_CODECONTEXTITEM']._serialized_end=2018
  _globals['_CODECONTEXTITEM_SNIPPETBYTYPEENTRY']._serialized_start=1867
  _globals['_CODECONTEXTITEM_SNIPPETBYTYPEENTRY']._serialized_end=1976
  _globals['_SNIPPETWITHWORDCOUNT']._serialized_start=2021
  _globals['_SNIPPETWITHWORDCOUNT']._serialized_end=2298
  _globals['_SNIPPETWITHWORDCOUNT_WORDCOUNTBYSPLITTERENTRY']._serialized_start=2194
  _globals['_SNIPPETWITHWORDCOUNT_WORDCOUNTBYSPLITTERENTRY']._serialized_end=2298
  _globals['_WORDCOUNT']._serialized_start=2301
  _globals['_WORDCOUNT']._serialized_end=2467
  _globals['_WORDCOUNT_WORDCOUNTMAPENTRY']._serialized_start=2404
  _globals['_WORDCOUNT_WORDCOUNTMAPENTRY']._serialized_end=2467
  _globals['_WORKSPACEPATH']._serialized_start=2469
  _globals['_WORKSPACEPATH']._serialized_end=2551
  _globals['_USERSTATUS']._serialized_start=2554
  _globals['_USERSTATUS']._serialized_end=2813
  _globals['_EMBEDDINGMETADATA']._serialized_start=2816
  _globals['_EMBEDDINGMETADATA']._serialized_end=2987
  _globals['_USERSETTINGS']._serialized_start=2990
  _globals['_USERSETTINGS']._serialized_end=3158
  _globals['_GITREPOINFO']._serialized_start=3161
  _globals['_GITREPOINFO']._serialized_end=3411
  _globals['_EDITOROPTIONS']._serialized_start=3414
  _globals['_EDITOROPTIONS']._serialized_end=3566
# @@protoc_insertion_point(module_scope)
