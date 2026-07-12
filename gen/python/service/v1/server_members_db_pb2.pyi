from shared.v1 import files_pb2 as _files_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerMemberCompositeKey(_message.Message):
    __slots__ = ("server_id", "user_id")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    user_id: str
    def __init__(self, server_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ServerMember(_message.Message):
    __slots__ = ("server_id", "user_id", "username", "avatar", "nickname", "joined_at", "roles", "timeout", "can_publish", "can_receive")
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CAN_PUBLISH_FIELD_NUMBER: _ClassVar[int]
    CAN_RECEIVE_FIELD_NUMBER: _ClassVar[int]
    server_id: str
    user_id: str
    username: str
    avatar: _files_pb2.File
    nickname: str
    joined_at: int
    roles: _containers.RepeatedScalarFieldContainer[str]
    timeout: int
    can_publish: bool
    can_receive: bool
    def __init__(self, server_id: _Optional[str] = ..., user_id: _Optional[str] = ..., username: _Optional[str] = ..., avatar: _Optional[_Union[_files_pb2.File, _Mapping]] = ..., nickname: _Optional[str] = ..., joined_at: _Optional[int] = ..., roles: _Optional[_Iterable[str]] = ..., timeout: _Optional[int] = ..., can_publish: bool = ..., can_receive: bool = ...) -> None: ...
