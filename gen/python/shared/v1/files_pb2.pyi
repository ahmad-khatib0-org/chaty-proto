from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ("id", "uploader_id", "bucket", "filename", "content_type", "size", "hash", "uploaded_at", "deleted", "reported", "metadata", "is_spoiler")
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
    METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_SPOILER_FIELD_NUMBER: _ClassVar[int]
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
    metadata: FileMetadata
    is_spoiler: bool
    def __init__(self, id: _Optional[str] = ..., uploader_id: _Optional[str] = ..., bucket: _Optional[str] = ..., filename: _Optional[str] = ..., content_type: _Optional[str] = ..., size: _Optional[int] = ..., hash: _Optional[str] = ..., uploaded_at: _Optional[int] = ..., deleted: bool = ..., reported: bool = ..., metadata: _Optional[_Union[FileMetadata, _Mapping]] = ..., is_spoiler: bool = ...) -> None: ...

class FileMetadata(_message.Message):
    __slots__ = ("file", "text", "image", "video", "audio")
    FILE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    file: FileMetadataFile
    text: FileMetadataText
    image: FileMetadataImage
    video: FileMetadataVideo
    audio: FileMetadataAudio
    def __init__(self, file: _Optional[_Union[FileMetadataFile, _Mapping]] = ..., text: _Optional[_Union[FileMetadataText, _Mapping]] = ..., image: _Optional[_Union[FileMetadataImage, _Mapping]] = ..., video: _Optional[_Union[FileMetadataVideo, _Mapping]] = ..., audio: _Optional[_Union[FileMetadataAudio, _Mapping]] = ...) -> None: ...

class FileMetadataFile(_message.Message):
    __slots__ = ("file_type",)
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    file_type: str
    def __init__(self, file_type: _Optional[str] = ...) -> None: ...

class FileMetadataText(_message.Message):
    __slots__ = ("text_length",)
    TEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    text_length: str
    def __init__(self, text_length: _Optional[str] = ...) -> None: ...

class FileMetadataImage(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class FileMetadataVideo(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class FileMetadataAudio(_message.Message):
    __slots__ = ("audio_duration",)
    AUDIO_DURATION_FIELD_NUMBER: _ClassVar[int]
    audio_duration: int
    def __init__(self, audio_duration: _Optional[int] = ...) -> None: ...
