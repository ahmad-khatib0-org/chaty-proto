from service.v1 import roles_db_pb2 as _roles_db_pb2
from shared.v1 import files_pb2 as _files_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelGroup(_message.Message):
    __slots__ = ("user_id", "name", "description", "recipients", "icon", "last_message_id", "permissions", "nsfw")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NSFW_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    description: str
    recipients: _containers.RepeatedScalarFieldContainer[str]
    icon: _files_pb2.File
    last_message_id: str
    permissions: int
    nsfw: bool
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., recipients: _Optional[_Iterable[str]] = ..., icon: _Optional[_Union[_files_pb2.File, _Mapping]] = ..., last_message_id: _Optional[str] = ..., permissions: _Optional[int] = ..., nsfw: bool = ...) -> None: ...

class ChannelSavedMessages(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ChannelText(_message.Message):
    __slots__ = ("server_id", "name", "description", "icon", "last_message_id", "default_permissions", "role_permissions", "nsfw")
    class RolePermissionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _roles_db_pb2.OverrideField
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_roles_db_pb2.OverrideField, _Mapping]] = ...) -> None: ...
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ROLE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NSFW_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    name: str
    description: str
    icon: _files_pb2.File
    last_message_id: str
    default_permissions: _roles_db_pb2.OverrideField
    role_permissions: _containers.MessageMap[str, _roles_db_pb2.OverrideField]
    nsfw: bool
    def __init__(self, server_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[_Union[_files_pb2.File, _Mapping]] = ..., last_message_id: _Optional[str] = ..., default_permissions: _Optional[_Union[_roles_db_pb2.OverrideField, _Mapping]] = ..., role_permissions: _Optional[_Mapping[str, _roles_db_pb2.OverrideField]] = ..., nsfw: bool = ...) -> None: ...

class ChannelDirectMessage(_message.Message):
    __slots__ = ("active", "recipients", "last_message_id")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    recipients: _containers.RepeatedScalarFieldContainer[str]
    last_message_id: str
    def __init__(self, active: bool = ..., recipients: _Optional[_Iterable[str]] = ..., last_message_id: _Optional[str] = ...) -> None: ...

class Channel(_message.Message):
    __slots__ = ("id", "channel_type", "saved", "direct", "group", "text", "voice_max_users", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SAVED_FIELD_NUMBER: _ClassVar[int]
    DIRECT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VOICE_MAX_USERS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_type: str
    saved: ChannelSavedMessages
    direct: ChannelDirectMessage
    group: ChannelGroup
    text: ChannelText
    voice_max_users: int
    created_at: int
    updated_at: int
    def __init__(self, id: _Optional[str] = ..., channel_type: _Optional[str] = ..., saved: _Optional[_Union[ChannelSavedMessages, _Mapping]] = ..., direct: _Optional[_Union[ChannelDirectMessage, _Mapping]] = ..., group: _Optional[_Union[ChannelGroup, _Mapping]] = ..., text: _Optional[_Union[ChannelText, _Mapping]] = ..., voice_max_users: _Optional[int] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ...) -> None: ...
