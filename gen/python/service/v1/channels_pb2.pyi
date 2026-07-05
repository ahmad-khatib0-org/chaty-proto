from service.v1 import channels_db_pb2 as _channels_db_pb2
from shared.v1 import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelUnread(_message.Message):
    __slots__ = ("id", "last_id", "mentions")
    ID_FIELD_NUMBER: _ClassVar[int]
    LAST_ID_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    id: ChannelCompositeKey
    last_id: str
    mentions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Union[ChannelCompositeKey, _Mapping]] = ..., last_id: _Optional[str] = ..., mentions: _Optional[_Iterable[str]] = ...) -> None: ...

class ChannelCompositeKey(_message.Message):
    __slots__ = ("channel", "user")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    channel: str
    user: str
    def __init__(self, channel: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...

class ChannelsGetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ChannelsGetResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: _channels_db_pb2.Channel
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[_channels_db_pb2.Channel, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class ChannelsCreateRequest(_message.Message):
    __slots__ = ("channel_type", "name", "description", "nsfw", "voice_max_users")
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NSFW_FIELD_NUMBER: _ClassVar[int]
    VOICE_MAX_USERS_FIELD_NUMBER: _ClassVar[int]
    channel_type: str
    name: str
    description: str
    nsfw: bool
    voice_max_users: int
    def __init__(self, channel_type: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., nsfw: bool = ..., voice_max_users: _Optional[int] = ...) -> None: ...

class ChannelsCreateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
