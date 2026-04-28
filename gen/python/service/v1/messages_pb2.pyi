from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReplyIntent(_message.Message):
    __slots__ = ("id", "mention", "fail_if_not_exists")
    ID_FIELD_NUMBER: _ClassVar[int]
    MENTION_FIELD_NUMBER: _ClassVar[int]
    FAIL_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    mention: bool
    fail_if_not_exists: bool
    def __init__(self, id: _Optional[str] = ..., mention: bool = ..., fail_if_not_exists: bool = ...) -> None: ...
