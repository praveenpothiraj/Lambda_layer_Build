# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/holistic_landmarker/proto/holistic_result.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework.formats import classification_pb2 as mediapipe_dot_framework_dot_formats_dot_classification__pb2
from mediapipe.framework.formats import landmark_pb2 as mediapipe_dot_framework_dot_formats_dot_landmark__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nImediapipe/tasks/cc/vision/holistic_landmarker/proto/holistic_result.proto\x12\x30mediapipe.tasks.vision.holistic_landmarker.proto\x1a\x30mediapipe/framework/formats/classification.proto\x1a*mediapipe/framework/formats/landmark.proto\"\xb7\x03\n\x0eHolisticResult\x12\x39\n\x0epose_landmarks\x18\x01 \x01(\x0b\x32!.mediapipe.NormalizedLandmarkList\x12\x35\n\x14pose_world_landmarks\x18\x07 \x01(\x0b\x32\x17.mediapipe.LandmarkList\x12>\n\x13left_hand_landmarks\x18\x02 \x01(\x0b\x32!.mediapipe.NormalizedLandmarkList\x12?\n\x14right_hand_landmarks\x18\x03 \x01(\x0b\x32!.mediapipe.NormalizedLandmarkList\x12\x39\n\x0e\x66\x61\x63\x65_landmarks\x18\x04 \x01(\x0b\x32!.mediapipe.NormalizedLandmarkList\x12\x37\n\x10\x66\x61\x63\x65_blendshapes\x18\x06 \x01(\x0b\x32\x1d.mediapipe.ClassificationList\x12>\n\x13\x61uxiliary_landmarks\x18\x05 \x01(\x0b\x32!.mediapipe.NormalizedLandmarkListBK\n4com.google.mediapipe.tasks.vision.holisticlandmarkerB\x13HolisticResultProtob\x06proto3')



_HOLISTICRESULT = DESCRIPTOR.message_types_by_name['HolisticResult']
HolisticResult = _reflection.GeneratedProtocolMessageType('HolisticResult', (_message.Message,), {
  'DESCRIPTOR' : _HOLISTICRESULT,
  '__module__' : 'mediapipe.tasks.cc.vision.holistic_landmarker.proto.holistic_result_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.vision.holistic_landmarker.proto.HolisticResult)
  })
_sym_db.RegisterMessage(HolisticResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n4com.google.mediapipe.tasks.vision.holisticlandmarkerB\023HolisticResultProto'
  _HOLISTICRESULT._serialized_start=222
  _HOLISTICRESULT._serialized_end=661
# @@protoc_insertion_point(module_scope)
