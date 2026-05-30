from service.v1 import bots_db_pb2 as _bots_db_pb2
from service.v1 import users_db_pb2 as _users_db_pb2
from shared.v1 import error_pb2 as _error_pb2
from shared.v1 import files_pb2 as _files_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_FLAG_UNSPECIFIED: _ClassVar[UserFlag]
    USER_FLAG_SUSPENDED_UNTIL: _ClassVar[UserFlag]
    USER_FLAG_DELETED: _ClassVar[UserFlag]
    USER_FLAG_BANNED: _ClassVar[UserFlag]
    USER_FLAG_SPAM: _ClassVar[UserFlag]
USER_FLAG_UNSPECIFIED: UserFlag
USER_FLAG_SUSPENDED_UNTIL: UserFlag
USER_FLAG_DELETED: UserFlag
USER_FLAG_BANNED: UserFlag
USER_FLAG_SPAM: UserFlag

class APIUser(_message.Message):
    __slots__ = ("id", "username", "email", "relationship", "display_name", "badges", "status_text", "status_presence", "profile_content", "profile_background_id", "privileged", "suspended_until", "created_at", "updated_at", "verified", "avatar", "relations", "bot", "online")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
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
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    id: str
    username: str
    email: str
    relationship: str
    display_name: str
    badges: int
    status_text: str
    status_presence: _users_db_pb2.UserStatus
    profile_content: str
    profile_background_id: str
    privileged: bool
    suspended_until: int
    created_at: int
    updated_at: int
    verified: bool
    avatar: _files_pb2.File
    relations: _containers.RepeatedCompositeFieldContainer[_users_db_pb2.UserRelationship]
    bot: _bots_db_pb2.Bot
    online: bool
    def __init__(self, id: _Optional[str] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., relationship: _Optional[str] = ..., display_name: _Optional[str] = ..., badges: _Optional[int] = ..., status_text: _Optional[str] = ..., status_presence: _Optional[_Union[_users_db_pb2.UserStatus, str]] = ..., profile_content: _Optional[str] = ..., profile_background_id: _Optional[str] = ..., privileged: bool = ..., suspended_until: _Optional[int] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., verified: bool = ..., avatar: _Optional[_Union[_files_pb2.File, _Mapping]] = ..., relations: _Optional[_Iterable[_Union[_users_db_pb2.UserRelationship, _Mapping]]] = ..., bot: _Optional[_Union[_bots_db_pb2.Bot, _Mapping]] = ..., online: bool = ...) -> None: ...

class UsersCreateRequest(_message.Message):
    __slots__ = ("email", "password", "username")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    username: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class UsersCreateResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: UsersCreateResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[UsersCreateResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class UsersCreateResponseData(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UsersLoginRequest(_message.Message):
    __slots__ = ("email", "password", "mfa", "login_challenge")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MFA_FIELD_NUMBER: _ClassVar[int]
    LOGIN_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    mfa: str
    login_challenge: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., mfa: _Optional[str] = ..., login_challenge: _Optional[str] = ...) -> None: ...

class UsersLoginResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: UsersLoginResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[UsersLoginResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class UsersLoginResponseData(_message.Message):
    __slots__ = ("redirect_to",)
    REDIRECT_TO_FIELD_NUMBER: _ClassVar[int]
    redirect_to: str
    def __init__(self, redirect_to: _Optional[str] = ...) -> None: ...

class UsersEmailConfirmationRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class UsersEmailConfirmationResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: UsersEmailConfirmationResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[UsersEmailConfirmationResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class UsersEmailConfirmationResponseData(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UsersForgotPasswordRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class UsersForgotPasswordResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: UsersForgotPasswordResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[UsersForgotPasswordResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class UsersForgotPasswordResponseData(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UsersResetPasswordRequest(_message.Message):
    __slots__ = ("token", "password", "password_confirmation")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    token: str
    password: str
    password_confirmation: str
    def __init__(self, token: _Optional[str] = ..., password: _Optional[str] = ..., password_confirmation: _Optional[str] = ...) -> None: ...

class UsersResetPasswordResponse(_message.Message):
    __slots__ = ("data", "error")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    data: UsersResetPasswordResponseData
    error: _error_pb2.AppError
    def __init__(self, data: _Optional[_Union[UsersResetPasswordResponseData, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.AppError, _Mapping]] = ...) -> None: ...

class UsersResetPasswordResponseData(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
