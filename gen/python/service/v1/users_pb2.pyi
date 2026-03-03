from shared.v1 import error_pb2 as _error_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
