from service.v1 import roles_db_pb2 as _roles_db_pb2
from shared.v1 import error_pb2 as _error_pb2
from shared.v1 import files_pb2 as _files_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Server(_message.Message):
    __slots__ = ("id", "owner_id", "name", "description", "default_permissions", "icon", "banner", "flags", "nsfw", "analytics", "discoverable", "roles", "categories", "system_messages", "stats", "channels", "created_at", "updated_at")
    class RolesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _roles_db_pb2.Role
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_roles_db_pb2.Role, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    BANNER_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    NSFW_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_FIELD_NUMBER: _ClassVar[int]
    DISCOVERABLE_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    owner_id: str
    name: str
    description: str
    default_permissions: int
    icon: _files_pb2.File
    banner: _files_pb2.File
    flags: int
    nsfw: bool
    analytics: bool
    discoverable: bool
    roles: _containers.MessageMap[str, _roles_db_pb2.Role]
    categories: _containers.RepeatedCompositeFieldContainer[Category]
    system_messages: ServerSystemMessagesChannels
    stats: ServerStats
    channels: _containers.RepeatedScalarFieldContainer[str]
    created_at: int
    updated_at: int
    def __init__(self, id: _Optional[str] = ..., owner_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., default_permissions: _Optional[int] = ..., icon: _Optional[_Union[_files_pb2.File, _Mapping]] = ..., banner: _Optional[_Union[_files_pb2.File, _Mapping]] = ..., flags: _Optional[int] = ..., nsfw: bool = ..., analytics: bool = ..., discoverable: bool = ..., roles: _Optional[_Mapping[str, _roles_db_pb2.Role]] = ..., categories: _Optional[_Iterable[_Union[Category, _Mapping]]] = ..., system_messages: _Optional[_Union[ServerSystemMessagesChannels, _Mapping]] = ..., stats: _Optional[_Union[ServerStats, _Mapping]] = ..., channels: _Optional[_Iterable[str]] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ...) -> None: ...

class Category(_message.Message):
    __slots__ = ("id", "title", "channels")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    channels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., channels: _Optional[_Iterable[str]] = ...) -> None: ...

class ServerSystemMessagesChannels(_message.Message):
    __slots__ = ("user_joined", "user_left", "user_kicked", "user_banned")
    USER_JOINED_FIELD_NUMBER: _ClassVar[int]
    USER_LEFT_FIELD_NUMBER: _ClassVar[int]
    USER_KICKED_FIELD_NUMBER: _ClassVar[int]
    USER_BANNED_FIELD_NUMBER: _ClassVar[int]
    user_joined: str
    user_left: str
    user_kicked: str
    user_banned: str
    def __init__(self, user_joined: _Optional[str] = ..., user_left: _Optional[str] = ..., user_kicked: _Optional[str] = ..., user_banned: _Optional[str] = ...) -> None: ...

class ServerStats(_message.Message):
    __slots__ = ("members_count", "channels_count")
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_COUNT_FIELD_NUMBER: _ClassVar[int]
    members_count: int
    channels_count: int
    def __init__(self, members_count: _Optional[int] = ..., channels_count: _Optional[int] = ...) -> None: ...
