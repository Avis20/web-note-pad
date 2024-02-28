from enum import Enum

from app.exceptions import base as app_exceptions


class UserExceptionInfo(app_exceptions.ExceptionEnum, Enum):
    USER_ALREADY_EXISTS = "4000", "User already exists"
    USER_NOT_FOUND = "4001", "User not found"
    USER_FORBIDDEN = "4003", "Access Denied"


class UserException(app_exceptions.BaseAppException):
    """user exception"""

    class UserExistsException(app_exceptions.BaseConflictException):
        code: str = UserExceptionInfo.USER_ALREADY_EXISTS.code
        error: str = UserExceptionInfo.USER_ALREADY_EXISTS.error

    class UserNotFoundException(app_exceptions.BaseNotFoundException):
        code: str = UserExceptionInfo.USER_NOT_FOUND.code
        error: str = UserExceptionInfo.USER_NOT_FOUND.error

    class UserForbiddenException(app_exceptions.BaseForbiddenException):
        code: str = UserExceptionInfo.USER_FORBIDDEN.code
        error: str = UserExceptionInfo.USER_FORBIDDEN.error
