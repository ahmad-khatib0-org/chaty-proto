from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatyConfig(_message.Message):
    __slots__ = ("chaty_version", "features", "ws", "app", "vapid", "build")
    CHATY_VERSION_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    WS_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    VAPID_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    chaty_version: str
    features: ChatyFeatures
    ws: str
    app: str
    vapid: str
    build: BuildInformation
    def __init__(self, chaty_version: _Optional[str] = ..., features: _Optional[_Union[ChatyFeatures, _Mapping]] = ..., ws: _Optional[str] = ..., app: _Optional[str] = ..., vapid: _Optional[str] = ..., build: _Optional[_Union[BuildInformation, _Mapping]] = ...) -> None: ...

class ChatyFeatures(_message.Message):
    __slots__ = ("captcha", "email", "invite_only", "files", "proxy", "livekit")
    CAPTCHA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    INVITE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    PROXY_FIELD_NUMBER: _ClassVar[int]
    LIVEKIT_FIELD_NUMBER: _ClassVar[int]
    captcha: CaptchaFeature
    email: bool
    invite_only: bool
    files: Feature
    proxy: Feature
    livekit: VoiceFeature
    def __init__(self, captcha: _Optional[_Union[CaptchaFeature, _Mapping]] = ..., email: bool = ..., invite_only: bool = ..., files: _Optional[_Union[Feature, _Mapping]] = ..., proxy: _Optional[_Union[Feature, _Mapping]] = ..., livekit: _Optional[_Union[VoiceFeature, _Mapping]] = ...) -> None: ...

class CaptchaFeature(_message.Message):
    __slots__ = ("enabled", "key")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    key: str
    def __init__(self, enabled: bool = ..., key: _Optional[str] = ...) -> None: ...

class Feature(_message.Message):
    __slots__ = ("enabled", "url")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    url: str
    def __init__(self, enabled: bool = ..., url: _Optional[str] = ...) -> None: ...

class VoiceFeature(_message.Message):
    __slots__ = ("enabled", "nodes")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    nodes: _containers.RepeatedCompositeFieldContainer[VoiceNode]
    def __init__(self, enabled: bool = ..., nodes: _Optional[_Iterable[_Union[VoiceNode, _Mapping]]] = ...) -> None: ...

class VoiceNode(_message.Message):
    __slots__ = ("name", "lat", "lon", "public_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    lat: float
    lon: float
    public_url: str
    def __init__(self, name: _Optional[str] = ..., lat: _Optional[float] = ..., lon: _Optional[float] = ..., public_url: _Optional[str] = ...) -> None: ...

class BuildInformation(_message.Message):
    __slots__ = ("commit_sha", "commit_timestamp", "semver", "origin_url", "timestamp")
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    COMMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SEMVER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_URL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    commit_sha: str
    commit_timestamp: str
    semver: str
    origin_url: str
    timestamp: str
    def __init__(self, commit_sha: _Optional[str] = ..., commit_timestamp: _Optional[str] = ..., semver: _Optional[str] = ..., origin_url: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...
