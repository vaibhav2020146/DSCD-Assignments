# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\"\"\n\x0fServeClientArgs\x12\x0f\n\x07Request\x18\x01 \x01(\t\"C\n\x10ServeClientReply\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\t\x12\x10\n\x08LeaderID\x18\x02 \x01(\t\x12\x0f\n\x07Success\x18\x03 \x01(\x08\"d\n\x0fRequestVoteArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x14\n\x0c\x63\x61ndidate_id\x18\x02 \x01(\x05\x12\x16\n\x0elast_log_index\x18\x03 \x01(\x05\x12\x15\n\rlast_log_term\x18\x04 \x01(\x05\"6\n\x10RequestVoteReply\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x14\n\x0cvote_granted\x18\x02 \x01(\x08\"4\n\x08LogEntry\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\x94\x01\n\x0f\x41ppendEntryArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x11\n\tleader_id\x18\x02 \x01(\x05\x12\x16\n\x0eprev_log_index\x18\x03 \x01(\x05\x12\x15\n\rprev_log_term\x18\x04 \x01(\x05\x12\x1a\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\t.LogEntry\x12\x15\n\rleader_commit\x18\x06 \x01(\x05\"1\n\x10\x41ppendEntryReply\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\x32\xac\x01\n\x08RaftNode\x12\x34\n\x0bRequestVote\x12\x10.RequestVoteArgs\x1a\x11.RequestVoteReply\"\x00\x12\x34\n\x0b\x41ppendEntry\x12\x10.AppendEntryArgs\x1a\x11.AppendEntryReply\"\x00\x12\x34\n\x0bServeClient\x12\x10.ServeClientArgs\x1a\x11.ServeClientReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SERVECLIENTARGS']._serialized_start=14
  _globals['_SERVECLIENTARGS']._serialized_end=48
  _globals['_SERVECLIENTREPLY']._serialized_start=50
  _globals['_SERVECLIENTREPLY']._serialized_end=117
  _globals['_REQUESTVOTEARGS']._serialized_start=119
  _globals['_REQUESTVOTEARGS']._serialized_end=219
  _globals['_REQUESTVOTEREPLY']._serialized_start=221
  _globals['_REQUESTVOTEREPLY']._serialized_end=275
  _globals['_LOGENTRY']._serialized_start=277
  _globals['_LOGENTRY']._serialized_end=329
  _globals['_APPENDENTRYARGS']._serialized_start=332
  _globals['_APPENDENTRYARGS']._serialized_end=480
  _globals['_APPENDENTRYREPLY']._serialized_start=482
  _globals['_APPENDENTRYREPLY']._serialized_end=531
  _globals['_RAFTNODE']._serialized_start=534
  _globals['_RAFTNODE']._serialized_end=706
# @@protoc_insertion_point(module_scope)
