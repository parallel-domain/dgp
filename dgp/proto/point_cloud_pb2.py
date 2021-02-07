# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dgp/proto/point_cloud.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dgp.proto import geometry_pb2 as dgp_dot_proto_dot_geometry__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dgp/proto/point_cloud.proto',
  package='dgp.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x64gp/proto/point_cloud.proto\x12\tdgp.proto\x1a\x18\x64gp/proto/geometry.proto\x1a\x19google/protobuf/any.proto\"\xa6\x04\n\nPointCloud\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12;\n\x0b\x61nnotations\x18\x02 \x03(\x0b\x32&.dgp.proto.PointCloud.AnnotationsEntry\x12\x35\n\x08metadata\x18\x03 \x03(\x0b\x32#.dgp.proto.PointCloud.MetadataEntry\x12\x37\n\x0cpoint_format\x18\x04 \x03(\x0e\x32!.dgp.proto.PointCloud.ChannelType\x12\x14\n\x0cpoint_fields\x18\x05 \x03(\t\x12\x1d\n\x04pose\x18\x06 \x01(\x0b\x32\x0f.dgp.proto.Pose\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x45\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"\xa8\x01\n\x0b\x43hannelType\x12\x05\n\x01X\x10\x00\x12\x05\n\x01Y\x10\x01\x12\x05\n\x01Z\x10\x02\x12\r\n\tINTENSITY\x10\x03\x12\x05\n\x01R\x10\x04\x12\x05\n\x01G\x10\x05\x12\x05\n\x01\x42\x10\x06\x12\x08\n\x04RING\x10\x07\x12\x0c\n\x08NORMAL_X\x10\x08\x12\x0c\n\x08NORMAL_Y\x10\t\x12\x0c\n\x08NORMAL_Z\x10\n\x12\x0c\n\x08\x43LASS_ID\x10\x0b\x12\x0f\n\x0bINSTANCE_ID\x10\x0c\x12\r\n\tTIMESTAMP\x10\rb\x06proto3'
  ,
  dependencies=[dgp_dot_proto_dot_geometry__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])



_POINTCLOUD_CHANNELTYPE = _descriptor.EnumDescriptor(
  name='ChannelType',
  full_name='dgp.proto.PointCloud.ChannelType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='X', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Y', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Z', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTENSITY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='R', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='G', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='B', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RING', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NORMAL_X', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NORMAL_Y', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NORMAL_Z', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLASS_ID', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSTANCE_ID', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=478,
  serialized_end=646,
)
_sym_db.RegisterEnumDescriptor(_POINTCLOUD_CHANNELTYPE)


_POINTCLOUD_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='dgp.proto.PointCloud.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dgp.proto.PointCloud.AnnotationsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dgp.proto.PointCloud.AnnotationsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=404,
)

_POINTCLOUD_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='dgp.proto.PointCloud.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dgp.proto.PointCloud.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dgp.proto.PointCloud.MetadataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=475,
)

_POINTCLOUD = _descriptor.Descriptor(
  name='PointCloud',
  full_name='dgp.proto.PointCloud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='dgp.proto.PointCloud.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='dgp.proto.PointCloud.annotations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='dgp.proto.PointCloud.metadata', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point_format', full_name='dgp.proto.PointCloud.point_format', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point_fields', full_name='dgp.proto.PointCloud.point_fields', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='dgp.proto.PointCloud.pose', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_POINTCLOUD_ANNOTATIONSENTRY, _POINTCLOUD_METADATAENTRY, ],
  enum_types=[
    _POINTCLOUD_CHANNELTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=646,
)

_POINTCLOUD_ANNOTATIONSENTRY.containing_type = _POINTCLOUD
_POINTCLOUD_METADATAENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_POINTCLOUD_METADATAENTRY.containing_type = _POINTCLOUD
_POINTCLOUD.fields_by_name['annotations'].message_type = _POINTCLOUD_ANNOTATIONSENTRY
_POINTCLOUD.fields_by_name['metadata'].message_type = _POINTCLOUD_METADATAENTRY
_POINTCLOUD.fields_by_name['point_format'].enum_type = _POINTCLOUD_CHANNELTYPE
_POINTCLOUD.fields_by_name['pose'].message_type = dgp_dot_proto_dot_geometry__pb2._POSE
_POINTCLOUD_CHANNELTYPE.containing_type = _POINTCLOUD
DESCRIPTOR.message_types_by_name['PointCloud'] = _POINTCLOUD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PointCloud = _reflection.GeneratedProtocolMessageType('PointCloud', (_message.Message,), {

  'AnnotationsEntry' : _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), {
    'DESCRIPTOR' : _POINTCLOUD_ANNOTATIONSENTRY,
    '__module__' : 'dgp.proto.point_cloud_pb2'
    # @@protoc_insertion_point(class_scope:dgp.proto.PointCloud.AnnotationsEntry)
    })
  ,

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _POINTCLOUD_METADATAENTRY,
    '__module__' : 'dgp.proto.point_cloud_pb2'
    # @@protoc_insertion_point(class_scope:dgp.proto.PointCloud.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _POINTCLOUD,
  '__module__' : 'dgp.proto.point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:dgp.proto.PointCloud)
  })
_sym_db.RegisterMessage(PointCloud)
_sym_db.RegisterMessage(PointCloud.AnnotationsEntry)
_sym_db.RegisterMessage(PointCloud.MetadataEntry)


_POINTCLOUD_ANNOTATIONSENTRY._options = None
_POINTCLOUD_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
