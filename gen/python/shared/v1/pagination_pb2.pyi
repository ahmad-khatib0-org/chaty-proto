from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SortDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_DIRECTION_UNSPECIFIED: _ClassVar[SortDirection]
    SORT_DIRECTION_ASC: _ClassVar[SortDirection]
    SORT_DIRECTION_DESC: _ClassVar[SortDirection]
SORT_DIRECTION_UNSPECIFIED: SortDirection
SORT_DIRECTION_ASC: SortDirection
SORT_DIRECTION_DESC: SortDirection

class PaginationSort(_message.Message):
    __slots__ = ("name", "direction")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    direction: SortDirection
    def __init__(self, name: _Optional[str] = ..., direction: _Optional[_Union[SortDirection, str]] = ...) -> None: ...

class PaginationRequest(_message.Message):
    __slots__ = ("last_id", "page", "page_size", "page_token", "after", "after_including", "before", "before_including", "created_after", "created_before", "updated_after", "updated_before", "sort_by")
    LAST_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    AFTER_INCLUDING_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_INCLUDING_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    last_id: str
    page: int
    page_size: int
    page_token: str
    after: str
    after_including: str
    before: str
    before_including: str
    created_after: int
    created_before: int
    updated_after: int
    updated_before: int
    sort_by: _containers.RepeatedCompositeFieldContainer[PaginationSort]
    def __init__(self, last_id: _Optional[str] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., after: _Optional[str] = ..., after_including: _Optional[str] = ..., before: _Optional[str] = ..., before_including: _Optional[str] = ..., created_after: _Optional[int] = ..., created_before: _Optional[int] = ..., updated_after: _Optional[int] = ..., updated_before: _Optional[int] = ..., sort_by: _Optional[_Iterable[_Union[PaginationSort, _Mapping]]] = ...) -> None: ...

class PaginationResponse(_message.Message):
    __slots__ = ("next_page_token", "previous_page_token", "has_next", "has_previous")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_NEXT_FIELD_NUMBER: _ClassVar[int]
    HAS_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    previous_page_token: str
    has_next: bool
    has_previous: bool
    def __init__(self, next_page_token: _Optional[str] = ..., previous_page_token: _Optional[str] = ..., has_next: bool = ..., has_previous: bool = ...) -> None: ...
