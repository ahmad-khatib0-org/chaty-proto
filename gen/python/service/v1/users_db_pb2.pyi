from service.v1 import bots_db_pb2 as _bots_db_pb2
from shared.v1 import files_pb2 as _files_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_STATUS_ONLINE: _ClassVar[UserStatus]
    USER_STATUS_IDLE: _ClassVar[UserStatus]
    USER_STATUS_FOCUS: _ClassVar[UserStatus]
    USER_STATUS_BUSY: _ClassVar[UserStatus]
    USER_STATUS_INVISIBLE: _ClassVar[UserStatus]

class UserRelationshipStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_RELATIONSHIP_STATUS_NONE: _ClassVar[UserRelationshipStatus]
    USER_RELATIONSHIP_STATUS_USER: _ClassVar[UserRelationshipStatus]
    USER_RELATIONSHIP_STATUS_FRIEND: _ClassVar[UserRelationshipStatus]
    USER_RELATIONSHIP_STATUS_OUTGOING: _ClassVar[UserRelationshipStatus]
    USER_RELATIONSHIP_STATUS_INCOMING: _ClassVar[UserRelationshipStatus]
    USER_RELATIONSHIP_STATUS_BLOCKED: _ClassVar[UserRelationshipStatus]
    USER_RELATIONSHIP_STATUS_BLOCKED_OTHER: _ClassVar[UserRelationshipStatus]
USER_STATUS_ONLINE: UserStatus
USER_STATUS_IDLE: UserStatus
USER_STATUS_FOCUS: UserStatus
USER_STATUS_BUSY: UserStatus
USER_STATUS_INVISIBLE: UserStatus
USER_RELATIONSHIP_STATUS_NONE: UserRelationshipStatus
USER_RELATIONSHIP_STATUS_USER: UserRelationshipStatus
USER_RELATIONSHIP_STATUS_FRIEND: UserRelationshipStatus
USER_RELATIONSHIP_STATUS_OUTGOING: UserRelationshipStatus
USER_RELATIONSHIP_STATUS_INCOMING: UserRelationshipStatus
USER_RELATIONSHIP_STATUS_BLOCKED: UserRelationshipStatus
USER_RELATIONSHIP_STATUS_BLOCKED_OTHER: UserRelationshipStatus

class User(_message.Message):
    __slots__ = ("id", "username", "email", "password", "display_name", "badges", "status_text", "status_presence", "profile_content", "profile_background_id", "privileged", "suspended_until", "created_at", "updated_at", "verified", "avatar", "relations", "bot")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BADGES_FIELD_NUMBER: _ClassVar[int]
    STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
    STATUS_PRESENCE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    PROFILE_BACKGROUND_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGED_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_UNTIL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    BOT_FIELD_NUMBER: _ClassVar[int]
    id: str
    username: str
    email: str
    password: str
    display_name: str
    badges: int
    status_text: str
    status_presence: UserStatus
    profile_content: str
    profile_background_id: str
    privileged: bool
    suspended_until: int
    created_at: int
    updated_at: int
    verified: bool
    avatar: _files_pb2.File
    relations: _containers.RepeatedCompositeFieldContainer[UserRelationship]
    bot: _bots_db_pb2.Bot
    def __init__(self, id: _Optional[str] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., display_name: _Optional[str] = ..., badges: _Optional[int] = ..., status_text: _Optional[str] = ..., status_presence: _Optional[_Union[UserStatus, str]] = ..., profile_content: _Optional[str] = ..., profile_background_id: _Optional[str] = ..., privileged: bool = ..., suspended_until: _Optional[int] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., verified: bool = ..., avatar: _Optional[_Union[_files_pb2.File, _Mapping]] = ..., relations: _Optional[_Iterable[_Union[UserRelationship, _Mapping]]] = ..., bot: _Optional[_Union[_bots_db_pb2.Bot, _Mapping]] = ...) -> None: ...

class UserRelationship(_message.Message):
    __slots__ = ("id", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: UserRelationshipStatus
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[UserRelationshipStatus, str]] = ...) -> None: ...
