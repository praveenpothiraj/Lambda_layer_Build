# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/align_hand_to_pose_in_world_calculator.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGmediapipe/calculators/util/align_hand_to_pose_in_world_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xbc\x01\n\'AlignHandToPoseInWorldCalculatorOptions\x12\x16\n\x0ehand_wrist_idx\x18\x01 \x01(\x05\x12\x16\n\x0epose_wrist_idx\x18\x02 \x01(\x05\x32\x61\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xca\xcf\xb0\xc0\x01 \x01(\x0b\x32\x32.mediapipe.AlignHandToPoseInWorldCalculatorOptions')



_ALIGNHANDTOPOSEINWORLDCALCULATOROPTIONS = DESCRIPTOR.message_types_by_name['AlignHandToPoseInWorldCalculatorOptions']
AlignHandToPoseInWorldCalculatorOptions = _reflection.GeneratedProtocolMessageType('AlignHandToPoseInWorldCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _ALIGNHANDTOPOSEINWORLDCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.util.align_hand_to_pose_in_world_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.AlignHandToPoseInWorldCalculatorOptions)
  })
_sym_db.RegisterMessage(AlignHandToPoseInWorldCalculatorOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_ALIGNHANDTOPOSEINWORLDCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _ALIGNHANDTOPOSEINWORLDCALCULATOROPTIONS._serialized_start=125
  _ALIGNHANDTOPOSEINWORLDCALCULATOROPTIONS._serialized_end=313
# @@protoc_insertion_point(module_scope)
