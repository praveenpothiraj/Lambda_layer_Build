# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/tool/node_chain_subgraph.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2mediapipe/framework/tool/node_chain_subgraph.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x96\x01\n\x18NodeChainSubgraphOptions\x12\x11\n\tnode_type\x18\x01 \x01(\t\x12\x14\n\x0c\x63hain_length\x18\x02 \x01(\x05\x32Q\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xd3\xdc\xddO \x01(\x0b\x32#.mediapipe.NodeChainSubgraphOptions')



_NODECHAINSUBGRAPHOPTIONS = DESCRIPTOR.message_types_by_name['NodeChainSubgraphOptions']
NodeChainSubgraphOptions = _reflection.GeneratedProtocolMessageType('NodeChainSubgraphOptions', (_message.Message,), {
  'DESCRIPTOR' : _NODECHAINSUBGRAPHOPTIONS,
  '__module__' : 'mediapipe.framework.tool.node_chain_subgraph_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.NodeChainSubgraphOptions)
  })
_sym_db.RegisterMessage(NodeChainSubgraphOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_NODECHAINSUBGRAPHOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _NODECHAINSUBGRAPHOPTIONS._serialized_start=104
  _NODECHAINSUBGRAPHOPTIONS._serialized_end=254
# @@protoc_insertion_point(module_scope)