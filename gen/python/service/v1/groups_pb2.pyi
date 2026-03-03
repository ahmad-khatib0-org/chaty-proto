from service.v1 import channels_db_pb2 as _channels_db_pb2
from shared.v1 import error_pb2 as _error_pb2
from shared.v1 import pagination_pb2 as _pagination_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupsCreateRequest(_message.Message):
    __slots__ = ("name", "description", "recipients", "nsfw")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    NSFW_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    recipients: _containers.RepeatedScalarFieldContainer[str]
    nsfw: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., recipients: _Optional[_Iterable[str]] = ..., nsfw: bool = ...) -> None: ...

class GroupsCreateResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: GroupsCreateResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[GroupsCreateResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class GroupsCreateResponseData(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GroupsListRequest(_message.Message):
    __slots__ = ("pagination",)
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    pagination: _pagination_pb2.PaginationRequest
    def __init__(self, pagination: _Optional[_Union[_pagination_pb2.PaginationRequest, _Mapping]] = ...) -> None: ...

class GroupsListResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: GroupsListResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[GroupsListResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class GroupsListResponseData(_message.Message):
    __slots__ = ("groups", "pagination")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[GroupsListItem]
    pagination: _pagination_pb2.PaginationResponse
    def __init__(self, groups: _Optional[_Iterable[_Union[GroupsListItem, _Mapping]]] = ..., pagination: _Optional[_Union[_pagination_pb2.PaginationResponse, _Mapping]] = ...) -> None: ...

class GroupsListItem(_message.Message):
    __slots__ = ("id", "group", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    group: _channels_db_pb2.ChannelGroup
    created_at: int
    def __init__(self, id: _Optional[str] = ..., group: _Optional[_Union[_channels_db_pb2.ChannelGroup, _Mapping]] = ..., created_at: _Optional[int] = ...) -> None: ...
