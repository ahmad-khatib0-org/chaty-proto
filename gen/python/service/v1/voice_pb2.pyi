from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserVoiceState(_message.Message):
    __slots__ = ("id", "joined_at", "is_receiving", "is_publishing", "screensharing", "camera")
    ID_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_RECEIVING_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHING_FIELD_NUMBER: _ClassVar[int]
    SCREENSHARING_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FIELD_NUMBER: _ClassVar[int]
    id: str
    joined_at: int
    is_receiving: bool
    is_publishing: bool
    screensharing: bool
    camera: bool
    def __init__(self, id: _Optional[str] = ..., joined_at: _Optional[int] = ..., is_receiving: bool = ..., is_publishing: bool = ..., screensharing: bool = ..., camera: bool = ...) -> None: ...
