from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Emoji(_message.Message):
    __slots__ = ("id", "parent", "creator_id", "name", "animated", "nsfw")
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANIMATED_FIELD_NUMBER: _ClassVar[int]
    NSFW_FIELD_NUMBER: _ClassVar[int]
    id: str
    parent: EmojiParent
    creator_id: str
    name: str
    animated: bool
    nsfw: bool
    def __init__(self, id: _Optional[str] = ..., parent: _Optional[_Union[EmojiParent, _Mapping]] = ..., creator_id: _Optional[str] = ..., name: _Optional[str] = ..., animated: bool = ..., nsfw: bool = ...) -> None: ...

class EmojiParent(_message.Message):
    __slots__ = ("server", "detached")
    SERVER_FIELD_NUMBER: _ClassVar[int]
    DETACHED_FIELD_NUMBER: _ClassVar[int]
    server: EmojiParentServer
    detached: EmojiParentDetached
    def __init__(self, server: _Optional[_Union[EmojiParentServer, _Mapping]] = ..., detached: _Optional[_Union[EmojiParentDetached, _Mapping]] = ...) -> None: ...

class EmojiParentServer(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EmojiParentDetached(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
