from service.v1 import messages_pb2 as _messages_pb2
from service.v1 import messages_db_pb2 as _messages_db_pb2
from service.v1 import server_members_db_pb2 as _server_members_db_pb2
from service.v1 import users_pb2 as _users_pb2
from shared.v1 import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchUsernamesRequest(_message.Message):
    __slots__ = ("query", "limit")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    query: str
    limit: int
    def __init__(self, query: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class SearchUsernamesResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: SearchUsernamesResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[SearchUsernamesResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class SearchUsernamesResponseData(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[SearchUser]
    def __init__(self, users: _Optional[_Iterable[_Union[SearchUser, _Mapping]]] = ...) -> None: ...

class SearchUser(_message.Message):
    __slots__ = ("id", "username", "display_name", "avatar")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    id: str
    username: str
    display_name: str
    avatar: str
    def __init__(self, id: _Optional[str] = ..., username: _Optional[str] = ..., display_name: _Optional[str] = ..., avatar: _Optional[str] = ...) -> None: ...

class SearchMessageRequest(_message.Message):
    __slots__ = ("query", "pinned", "limit", "before", "after", "sort", "include_users")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_USERS_FIELD_NUMBER: _ClassVar[int]
    query: str
    pinned: bool
    limit: int
    before: str
    after: str
    sort: _messages_pb2.MessageSort
    include_users: bool
    def __init__(self, query: _Optional[str] = ..., pinned: bool = ..., limit: _Optional[int] = ..., before: _Optional[str] = ..., after: _Optional[str] = ..., sort: _Optional[_Union[_messages_pb2.MessageSort, str]] = ..., include_users: bool = ...) -> None: ...

class SearchMessageResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: SearchMessageResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[SearchMessageResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class SearchMessageResponseData(_message.Message):
    __slots__ = ("messages", "users", "members")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_messages_db_pb2.Message]
    users: _containers.RepeatedCompositeFieldContainer[_users_pb2.APIUser]
    members: _containers.RepeatedCompositeFieldContainer[_server_members_db_pb2.ServerMember]
    def __init__(self, messages: _Optional[_Iterable[_Union[_messages_db_pb2.Message, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_users_pb2.APIUser, _Mapping]]] = ..., members: _Optional[_Iterable[_Union[_server_members_db_pb2.ServerMember, _Mapping]]] = ...) -> None: ...
