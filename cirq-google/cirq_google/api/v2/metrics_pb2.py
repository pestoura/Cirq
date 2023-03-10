# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cirq_google/api/v2/metrics.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cirq_google/api/v2/metrics.proto',
  package='cirq.google.api.v2',
  syntax='proto3',
  serialized_options=b'\n\035com.google.cirq.google.api.v2B\020CalibrationProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n cirq_google/api/v2/metrics.proto\x12\x12\x63irq.google.api.v2\"T\n\x0fMetricsSnapshot\x12\x14\n\x0ctimestamp_ms\x18\x01 \x01(\x04\x12+\n\x07metrics\x18\x02 \x03(\x0b\x32\x1a.cirq.google.api.v2.Metric\"R\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07targets\x18\x02 \x03(\t\x12)\n\x06values\x18\x03 \x03(\x0b\x32\x19.cirq.google.api.v2.Value\"a\n\x05Value\x12\x14\n\ndouble_val\x18\x01 \x01(\x01H\x00\x12\x13\n\tint32_val\x18\x02 \x01(\x05H\x00\x12\x13\n\tint64_val\x18\x03 \x01(\x03H\x00\x12\x11\n\x07str_val\x18\x04 \x01(\tH\x00\x42\x05\n\x03valB3\n\x1d\x63om.google.cirq.google.api.v2B\x10\x43\x61librationProtoP\x01\x62\x06proto3'
)




_METRICSSNAPSHOT = _descriptor.Descriptor(
  name='MetricsSnapshot',
  full_name='cirq.google.api.v2.MetricsSnapshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='cirq.google.api.v2.MetricsSnapshot.timestamp_ms', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='cirq.google.api.v2.MetricsSnapshot.metrics', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=140,
)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='cirq.google.api.v2.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cirq.google.api.v2.Metric.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targets', full_name='cirq.google.api.v2.Metric.targets', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='cirq.google.api.v2.Metric.values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=224,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='cirq.google.api.v2.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='double_val', full_name='cirq.google.api.v2.Value.double_val', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int32_val', full_name='cirq.google.api.v2.Value.int32_val', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_val', full_name='cirq.google.api.v2.Value.int64_val', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='str_val', full_name='cirq.google.api.v2.Value.str_val', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='val', full_name='cirq.google.api.v2.Value.val',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=226,
  serialized_end=323,
)

_METRICSSNAPSHOT.fields_by_name['metrics'].message_type = _METRIC
_METRIC.fields_by_name['values'].message_type = _VALUE
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['double_val'])
_VALUE.fields_by_name['double_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['int32_val'])
_VALUE.fields_by_name['int32_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['int64_val'])
_VALUE.fields_by_name['int64_val'].containing_oneof = _VALUE.oneofs_by_name['val']
_VALUE.oneofs_by_name['val'].fields.append(
  _VALUE.fields_by_name['str_val'])
_VALUE.fields_by_name['str_val'].containing_oneof = _VALUE.oneofs_by_name['val']
DESCRIPTOR.message_types_by_name['MetricsSnapshot'] = _METRICSSNAPSHOT
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetricsSnapshot = _reflection.GeneratedProtocolMessageType('MetricsSnapshot', (_message.Message,), {
  'DESCRIPTOR' : _METRICSSNAPSHOT,
  '__module__' : 'cirq_google.api.v2.metrics_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v2.MetricsSnapshot)
  })
_sym_db.RegisterMessage(MetricsSnapshot)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'cirq_google.api.v2.metrics_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v2.Metric)
  })
_sym_db.RegisterMessage(Metric)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'cirq_google.api.v2.metrics_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v2.Value)
  })
_sym_db.RegisterMessage(Value)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
