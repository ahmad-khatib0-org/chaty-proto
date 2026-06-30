from shared.v1 import error_pb2 as _error_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServersCreateRequest(_message.Message):
    __slots__ = ("name", "description", "nsfw")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NSFW_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    nsfw: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., nsfw: bool = ...) -> None: ...

class ServersCreateResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: ServersCreateResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[ServersCreateResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class ServersCreateResponseData(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
