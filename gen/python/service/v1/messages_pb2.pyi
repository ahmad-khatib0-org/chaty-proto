from service.v1 import messages_db_pb2 as _messages_db_pb2
from service.v1 import server_members_db_pb2 as _server_members_db_pb2
from service.v1 import users_pb2 as _users_pb2
from shared.v1 import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageSort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_SORT_UNSPECIFIED: _ClassVar[MessageSort]
    MESSAGE_SORT_LATEST: _ClassVar[MessageSort]
    MESSAGE_SORT_OLDEST: _ClassVar[MessageSort]
    MESSAGE_SORT_RELEVANCE: _ClassVar[MessageSort]
MESSAGE_SORT_UNSPECIFIED: MessageSort
MESSAGE_SORT_LATEST: MessageSort
MESSAGE_SORT_OLDEST: MessageSort
MESSAGE_SORT_RELEVANCE: MessageSort

class ReplyIntent(_message.Message):
    __slots__ = ("id", "mention", "fail_if_not_exists")
    ID_FIELD_NUMBER: _ClassVar[int]
    MENTION_FIELD_NUMBER: _ClassVar[int]
    FAIL_IF_NOT_EXISTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    mention: bool
    fail_if_not_exists: bool
    def __init__(self, id: _Optional[str] = ..., mention: bool = ..., fail_if_not_exists: bool = ...) -> None: ...

class MessagesGetRequest(_message.Message):
    __slots__ = ("channel_id", "limit", "before", "after", "sort", "nearby")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    NEARBY_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    limit: int
    before: str
    after: str
    sort: MessageSort
    nearby: str
    def __init__(self, channel_id: _Optional[str] = ..., limit: _Optional[int] = ..., before: _Optional[str] = ..., after: _Optional[str] = ..., sort: _Optional[_Union[MessageSort, str]] = ..., nearby: _Optional[str] = ...) -> None: ...

class MessagesGetResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: MessagesGetResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[MessagesGetResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class MessagesGetResponseData(_message.Message):
    __slots__ = ("messages", "users", "members")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_messages_db_pb2.Message]
    users: _containers.RepeatedCompositeFieldContainer[_users_pb2.APIUser]
    members: _containers.RepeatedCompositeFieldContainer[_server_members_db_pb2.ServerMember]
    def __init__(self, messages: _Optional[_Iterable[_Union[_messages_db_pb2.Message, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_users_pb2.APIUser, _Mapping]]] = ..., members: _Optional[_Iterable[_Union[_server_members_db_pb2.ServerMember, _Mapping]]] = ...) -> None: ...
