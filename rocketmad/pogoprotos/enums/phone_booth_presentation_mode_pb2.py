# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/phone_booth_presentation_mode.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/phone_booth_presentation_mode.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n4pogoprotos/enums/phone_booth_presentation_mode.proto\x12\x10pogoprotos.enums*[\n\x1aPhoneBoothPresentationMode\x12#\n\x1fNONE_PHONEBOLTHPRESENTATIONMODE\x10\x00\x12\x0c\n\x08PORTRAIT\x10\x01\x12\n\n\x06\x44IALOG\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PHONEBOOTHPRESENTATIONMODE = _descriptor.EnumDescriptor(
  name='PhoneBoothPresentationMode',
  full_name='pogoprotos.enums.PhoneBoothPresentationMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_PHONEBOLTHPRESENTATIONMODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PORTRAIT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIALOG', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=74,
  serialized_end=165,
)
_sym_db.RegisterEnumDescriptor(_PHONEBOOTHPRESENTATIONMODE)

PhoneBoothPresentationMode = enum_type_wrapper.EnumTypeWrapper(_PHONEBOOTHPRESENTATIONMODE)
NONE_PHONEBOLTHPRESENTATIONMODE = 0
PORTRAIT = 1
DIALOG = 2


DESCRIPTOR.enum_types_by_name['PhoneBoothPresentationMode'] = _PHONEBOOTHPRESENTATIONMODE


# @@protoc_insertion_point(module_scope)