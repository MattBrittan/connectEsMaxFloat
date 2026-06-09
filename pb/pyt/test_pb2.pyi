from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class exampleMessage(_message.Message):
    __slots__ = ("exampleFloat",)
    EXAMPLEFLOAT_FIELD_NUMBER: _ClassVar[int]
    exampleFloat: float
    def __init__(self, exampleFloat: _Optional[float] = ...) -> None: ...
