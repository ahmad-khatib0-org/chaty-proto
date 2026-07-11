from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ServerBan(_message.Message):
    __slots__ = ("server_id", "user_id", "reason", "banned_by", "banned_at")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    BANNED_BY_FIELD_NUMBER: _ClassVar[int]
    BANNED_AT_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    user_id: str
    reason: str
    banned_by: str
    banned_at: int
    def __init__(self, server_id: _Optional[str] = ..., user_id: _Optional[str] = ..., reason: _Optional[str] = ..., banned_by: _Optional[str] = ..., banned_at: _Optional[int] = ...) -> None: ...
