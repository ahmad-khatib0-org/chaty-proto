from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OverrideField(_message.Message):
    __slots__ = ("a", "d")
    A_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    a: int
    d: int
    def __init__(self, a: _Optional[int] = ..., d: _Optional[int] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("name", "permissions", "colour", "hoist", "rank", "created_at", "updated_at")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    COLOUR_FIELD_NUMBER: _ClassVar[int]
    HOIST_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    permissions: OverrideField
    colour: str
    hoist: bool
    rank: int
    created_at: int
    updated_at: int
    def __init__(self, name: _Optional[str] = ..., permissions: _Optional[_Union[OverrideField, _Mapping]] = ..., colour: _Optional[str] = ..., hoist: bool = ..., rank: _Optional[int] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ...) -> None: ...
