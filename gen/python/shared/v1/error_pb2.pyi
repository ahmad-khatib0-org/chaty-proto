from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AppError(_message.Message):
    __slots__ = ("id", "message", "detailed_error", "status_code", "location", "skip_translation", "errors")
    class ErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILED_ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SKIP_TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: str
    detailed_error: str
    status_code: int
    location: str
    skip_translation: bool
    errors: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ..., detailed_error: _Optional[str] = ..., status_code: _Optional[int] = ..., location: _Optional[str] = ..., skip_translation: bool = ..., errors: _Optional[_Mapping[str, str]] = ...) -> None: ...
