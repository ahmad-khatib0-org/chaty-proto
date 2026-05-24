from shared.v1 import files_pb2 as _files_pb2
from shared.v1 import types_pb2 as _types_pb2
from shared.v1 import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageWebhook(_message.Message):
    __slots__ = ("name", "avatar", "icon")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    name: str
    avatar: str
    icon: _files_pb2.File
    def __init__(self, name: _Optional[str] = ..., avatar: _Optional[str] = ..., icon: _Optional[_Union[_files_pb2.File, _Mapping]] = ...) -> None: ...

class MessageSystem(_message.Message):
    __slots__ = ("text", "user_added", "user_remove", "user_joined", "user_left", "user_kicked", "user_banned", "channel_renamed", "channel_description_changed", "channel_icon_changed", "channel_ownership_changed", "message_pinned", "message_unpinned", "call_started")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    USER_ADDED_FIELD_NUMBER: _ClassVar[int]
    USER_REMOVE_FIELD_NUMBER: _ClassVar[int]
    USER_JOINED_FIELD_NUMBER: _ClassVar[int]
    USER_LEFT_FIELD_NUMBER: _ClassVar[int]
    USER_KICKED_FIELD_NUMBER: _ClassVar[int]
    USER_BANNED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_RENAMED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_DESCRIPTION_CHANGED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ICON_CHANGED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_OWNERSHIP_CHANGED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_PINNED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_UNPINNED_FIELD_NUMBER: _ClassVar[int]
    CALL_STARTED_FIELD_NUMBER: _ClassVar[int]
    text: MessageSystemText
    user_added: MessageSystemUserAdded
    user_remove: MessageSystemUserRemove
    user_joined: MessageSystemUserJoined
    user_left: MessageSystemUserLeft
    user_kicked: MessageSystemUserKicked
    user_banned: MessageSystemUserBanned
    channel_renamed: MessageSystemChannelRenamed
    channel_description_changed: MessageSystemChannelDescriptionChanged
    channel_icon_changed: MessageSystemChannelIconChanged
    channel_ownership_changed: MessageSystemChannelOwnershipChanged
    message_pinned: MessageSystemMessagePinned
    message_unpinned: MessageSystemMessageUnpinned
    call_started: MessageSystemCallStarted
    def __init__(self, text: _Optional[_Union[MessageSystemText, _Mapping]] = ..., user_added: _Optional[_Union[MessageSystemUserAdded, _Mapping]] = ..., user_remove: _Optional[_Union[MessageSystemUserRemove, _Mapping]] = ..., user_joined: _Optional[_Union[MessageSystemUserJoined, _Mapping]] = ..., user_left: _Optional[_Union[MessageSystemUserLeft, _Mapping]] = ..., user_kicked: _Optional[_Union[MessageSystemUserKicked, _Mapping]] = ..., user_banned: _Optional[_Union[MessageSystemUserBanned, _Mapping]] = ..., channel_renamed: _Optional[_Union[MessageSystemChannelRenamed, _Mapping]] = ..., channel_description_changed: _Optional[_Union[MessageSystemChannelDescriptionChanged, _Mapping]] = ..., channel_icon_changed: _Optional[_Union[MessageSystemChannelIconChanged, _Mapping]] = ..., channel_ownership_changed: _Optional[_Union[MessageSystemChannelOwnershipChanged, _Mapping]] = ..., message_pinned: _Optional[_Union[MessageSystemMessagePinned, _Mapping]] = ..., message_unpinned: _Optional[_Union[MessageSystemMessageUnpinned, _Mapping]] = ..., call_started: _Optional[_Union[MessageSystemCallStarted, _Mapping]] = ...) -> None: ...

class MessageSystemText(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class MessageSystemUserAdded(_message.Message):
    __slots__ = ("id", "by")
    ID_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    by: str
    def __init__(self, id: _Optional[str] = ..., by: _Optional[str] = ...) -> None: ...

class MessageSystemUserRemove(_message.Message):
    __slots__ = ("id", "by")
    ID_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    by: str
    def __init__(self, id: _Optional[str] = ..., by: _Optional[str] = ...) -> None: ...

class MessageSystemUserJoined(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class MessageSystemUserLeft(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class MessageSystemUserKicked(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class MessageSystemUserBanned(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class MessageSystemChannelRenamed(_message.Message):
    __slots__ = ("name", "by")
    NAME_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    name: str
    by: str
    def __init__(self, name: _Optional[str] = ..., by: _Optional[str] = ...) -> None: ...

class MessageSystemChannelDescriptionChanged(_message.Message):
    __slots__ = ("by",)
    BY_FIELD_NUMBER: _ClassVar[int]
    by: str
    def __init__(self, by: _Optional[str] = ...) -> None: ...

class MessageSystemChannelIconChanged(_message.Message):
    __slots__ = ("by",)
    BY_FIELD_NUMBER: _ClassVar[int]
    by: str
    def __init__(self, by: _Optional[str] = ...) -> None: ...

class MessageSystemChannelOwnershipChanged(_message.Message):
    __slots__ = ("to",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: str
    def __init__(self, to: _Optional[str] = ..., **kwargs) -> None: ...

class MessageSystemMessagePinned(_message.Message):
    __slots__ = ("id", "by")
    ID_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    by: str
    def __init__(self, id: _Optional[str] = ..., by: _Optional[str] = ...) -> None: ...

class MessageSystemMessageUnpinned(_message.Message):
    __slots__ = ("id", "by")
    ID_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    by: str
    def __init__(self, id: _Optional[str] = ..., by: _Optional[str] = ...) -> None: ...

class MessageSystemCallStarted(_message.Message):
    __slots__ = ("by", "finished_at")
    BY_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    by: str
    finished_at: int
    def __init__(self, by: _Optional[str] = ..., finished_at: _Optional[int] = ...) -> None: ...

class EmbedImage(_message.Message):
    __slots__ = ("url", "width", "height", "size")
    URL_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    url: str
    width: int
    height: int
    size: str
    def __init__(self, url: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., size: _Optional[str] = ...) -> None: ...

class EmbedVideo(_message.Message):
    __slots__ = ("url", "width", "height")
    URL_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    url: str
    width: int
    height: int
    def __init__(self, url: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class TwitchType(_message.Message):
    __slots__ = ("channel", "video", "clip")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    CLIP_FIELD_NUMBER: _ClassVar[int]
    channel: str
    video: str
    clip: str
    def __init__(self, channel: _Optional[str] = ..., video: _Optional[str] = ..., clip: _Optional[str] = ...) -> None: ...

class LightspeedType(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: str
    def __init__(self, channel: _Optional[str] = ...) -> None: ...

class BandcampType(_message.Message):
    __slots__ = ("album", "track")
    ALBUM_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    album: str
    track: str
    def __init__(self, album: _Optional[str] = ..., track: _Optional[str] = ...) -> None: ...

class EmbedWebsiteMetadataSpecial(_message.Message):
    __slots__ = ("none", "gif", "youtube", "lightspeed", "twitch", "spotify", "soundcloud", "bandcamp", "apple_music", "streamable")
    NONE_FIELD_NUMBER: _ClassVar[int]
    GIF_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_FIELD_NUMBER: _ClassVar[int]
    LIGHTSPEED_FIELD_NUMBER: _ClassVar[int]
    TWITCH_FIELD_NUMBER: _ClassVar[int]
    SPOTIFY_FIELD_NUMBER: _ClassVar[int]
    SOUNDCLOUD_FIELD_NUMBER: _ClassVar[int]
    BANDCAMP_FIELD_NUMBER: _ClassVar[int]
    APPLE_MUSIC_FIELD_NUMBER: _ClassVar[int]
    STREAMABLE_FIELD_NUMBER: _ClassVar[int]
    none: _wrappers_pb2.Empty
    gif: _wrappers_pb2.Empty
    youtube: EmbedYouTube
    lightspeed: EmbedLightspeed
    twitch: EmbedTwitch
    spotify: EmbedSpotify
    soundcloud: _wrappers_pb2.Empty
    bandcamp: EmbedBandcamp
    apple_music: EmbedAppleMusic
    streamable: EmbedStreamable
    def __init__(self, none: _Optional[_Union[_wrappers_pb2.Empty, _Mapping]] = ..., gif: _Optional[_Union[_wrappers_pb2.Empty, _Mapping]] = ..., youtube: _Optional[_Union[EmbedYouTube, _Mapping]] = ..., lightspeed: _Optional[_Union[EmbedLightspeed, _Mapping]] = ..., twitch: _Optional[_Union[EmbedTwitch, _Mapping]] = ..., spotify: _Optional[_Union[EmbedSpotify, _Mapping]] = ..., soundcloud: _Optional[_Union[_wrappers_pb2.Empty, _Mapping]] = ..., bandcamp: _Optional[_Union[EmbedBandcamp, _Mapping]] = ..., apple_music: _Optional[_Union[EmbedAppleMusic, _Mapping]] = ..., streamable: _Optional[_Union[EmbedStreamable, _Mapping]] = ...) -> None: ...

class EmbedYouTube(_message.Message):
    __slots__ = ("id", "timestamp")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: str
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class EmbedLightspeed(_message.Message):
    __slots__ = ("content_type", "id")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    content_type: LightspeedType
    id: str
    def __init__(self, content_type: _Optional[_Union[LightspeedType, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class EmbedTwitch(_message.Message):
    __slots__ = ("content_type", "id")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    content_type: TwitchType
    id: str
    def __init__(self, content_type: _Optional[_Union[TwitchType, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class EmbedSpotify(_message.Message):
    __slots__ = ("content_type", "id")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    content_type: str
    id: str
    def __init__(self, content_type: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class EmbedBandcamp(_message.Message):
    __slots__ = ("content_type", "id")
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    content_type: BandcampType
    id: str
    def __init__(self, content_type: _Optional[_Union[BandcampType, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class EmbedAppleMusic(_message.Message):
    __slots__ = ("album_id", "track_id")
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    album_id: str
    track_id: str
    def __init__(self, album_id: _Optional[str] = ..., track_id: _Optional[str] = ...) -> None: ...

class EmbedStreamable(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EmbedWebsiteMetadata(_message.Message):
    __slots__ = ("url", "original_url", "special", "title", "description", "image", "video", "site_name", "icon_url", "colour")
    URL_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_URL_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    COLOUR_FIELD_NUMBER: _ClassVar[int]
    url: str
    original_url: str
    special: EmbedWebsiteMetadataSpecial
    title: str
    description: str
    image: EmbedImage
    video: EmbedVideo
    site_name: str
    icon_url: str
    colour: str
    def __init__(self, url: _Optional[str] = ..., original_url: _Optional[str] = ..., special: _Optional[_Union[EmbedWebsiteMetadataSpecial, _Mapping]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., image: _Optional[_Union[EmbedImage, _Mapping]] = ..., video: _Optional[_Union[EmbedVideo, _Mapping]] = ..., site_name: _Optional[str] = ..., icon_url: _Optional[str] = ..., colour: _Optional[str] = ...) -> None: ...

class EmbedText(_message.Message):
    __slots__ = ("icon_url", "url", "title", "description", "media", "colour")
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    COLOUR_FIELD_NUMBER: _ClassVar[int]
    icon_url: str
    url: str
    title: str
    description: str
    media: _files_pb2.File
    colour: str
    def __init__(self, icon_url: _Optional[str] = ..., url: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., media: _Optional[_Union[_files_pb2.File, _Mapping]] = ..., colour: _Optional[str] = ...) -> None: ...

class Embed(_message.Message):
    __slots__ = ("website", "image", "video", "text", "none")
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NONE_FIELD_NUMBER: _ClassVar[int]
    website: EmbedWebsiteMetadata
    image: EmbedImage
    video: EmbedVideo
    text: EmbedText
    none: _wrappers_pb2.Empty
    def __init__(self, website: _Optional[_Union[EmbedWebsiteMetadata, _Mapping]] = ..., image: _Optional[_Union[EmbedImage, _Mapping]] = ..., video: _Optional[_Union[EmbedVideo, _Mapping]] = ..., text: _Optional[_Union[EmbedText, _Mapping]] = ..., none: _Optional[_Union[_wrappers_pb2.Empty, _Mapping]] = ...) -> None: ...

class Interactions(_message.Message):
    __slots__ = ("reactions", "restrict_reactions")
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    reactions: _containers.RepeatedScalarFieldContainer[str]
    restrict_reactions: bool
    def __init__(self, reactions: _Optional[_Iterable[str]] = ..., restrict_reactions: bool = ...) -> None: ...

class Masquerade(_message.Message):
    __slots__ = ("name", "avatar", "colour")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    COLOUR_FIELD_NUMBER: _ClassVar[int]
    name: str
    avatar: str
    colour: str
    def __init__(self, name: _Optional[str] = ..., avatar: _Optional[str] = ..., colour: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("id", "channel_id", "nonce", "author_id", "webhook", "content", "system", "attachments", "flags", "embeds", "mentions", "role_mentions", "replies", "reactions", "interactions", "masquerade", "pinned", "edited_at", "created_at")
    class ReactionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _types_pb2.StringArray
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_types_pb2.StringArray, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    EMBEDS_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    ROLE_MENTIONS_FIELD_NUMBER: _ClassVar[int]
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    MASQUERADE_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    EDITED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_id: str
    nonce: str
    author_id: str
    webhook: MessageWebhook
    content: str
    system: MessageSystem
    attachments: _containers.RepeatedCompositeFieldContainer[_files_pb2.File]
    flags: int
    embeds: _containers.RepeatedCompositeFieldContainer[Embed]
    mentions: _containers.RepeatedScalarFieldContainer[str]
    role_mentions: _containers.RepeatedScalarFieldContainer[str]
    replies: _containers.RepeatedScalarFieldContainer[str]
    reactions: _containers.MessageMap[str, _types_pb2.StringArray]
    interactions: Interactions
    masquerade: Masquerade
    pinned: bool
    edited_at: int
    created_at: int
    def __init__(self, id: _Optional[str] = ..., channel_id: _Optional[str] = ..., nonce: _Optional[str] = ..., author_id: _Optional[str] = ..., webhook: _Optional[_Union[MessageWebhook, _Mapping]] = ..., content: _Optional[str] = ..., system: _Optional[_Union[MessageSystem, _Mapping]] = ..., attachments: _Optional[_Iterable[_Union[_files_pb2.File, _Mapping]]] = ..., flags: _Optional[int] = ..., embeds: _Optional[_Iterable[_Union[Embed, _Mapping]]] = ..., mentions: _Optional[_Iterable[str]] = ..., role_mentions: _Optional[_Iterable[str]] = ..., replies: _Optional[_Iterable[str]] = ..., reactions: _Optional[_Mapping[str, _types_pb2.StringArray]] = ..., interactions: _Optional[_Union[Interactions, _Mapping]] = ..., masquerade: _Optional[_Union[Masquerade, _Mapping]] = ..., pinned: bool = ..., edited_at: _Optional[int] = ..., created_at: _Optional[int] = ...) -> None: ...
