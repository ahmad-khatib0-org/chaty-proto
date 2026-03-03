from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ("id", "uploader_id", "bucket", "filename", "content_type", "size", "hash", "uploaded_at", "deleted", "reported")
    ID_FIELD_NUMBER: _ClassVar[int]
    UPLOADER_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    UPLOADED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    REPORTED_FIELD_NUMBER: _ClassVar[int]
    id: str
    uploader_id: str
    bucket: str
    filename: str
    content_type: str
    size: int
    hash: str
    uploaded_at: int
    deleted: bool
    reported: bool
    def __init__(self, id: _Optional[str] = ..., uploader_id: _Optional[str] = ..., bucket: _Optional[str] = ..., filename: _Optional[str] = ..., content_type: _Optional[str] = ..., size: _Optional[int] = ..., hash: _Optional[str] = ..., uploaded_at: _Optional[int] = ..., deleted: bool = ..., reported: bool = ...) -> None: ...
