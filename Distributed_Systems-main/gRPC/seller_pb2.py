# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: seller.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cseller.proto\"y\n\x1aReceiveNotificationRequest\x12\x1c\n\x14notification_message\x18\x01 \x01(\t\x12\x14\n\x0cproduct_name\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x15\n\rbuyer_address\x18\x04 \x01(\t\".\n\x1bReceiveNotificationResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\\\n\x06seller\x12R\n\x13ReceiveNotification\x12\x1b.ReceiveNotificationRequest\x1a\x1c.ReceiveNotificationResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'seller_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RECEIVENOTIFICATIONREQUEST']._serialized_start=16
  _globals['_RECEIVENOTIFICATIONREQUEST']._serialized_end=137
  _globals['_RECEIVENOTIFICATIONRESPONSE']._serialized_start=139
  _globals['_RECEIVENOTIFICATIONRESPONSE']._serialized_end=185
  _globals['_SELLER']._serialized_start=187
  _globals['_SELLER']._serialized_end=279
# @@protoc_insertion_point(module_scope)
