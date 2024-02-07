from enum import Enum

from app.exceptions.base import BaseAppException, ExceptionEnum


class UserExceptionInfo(ExceptionEnum, Enum):
    USER_ALREADY_EXISTS = "4000", "User already exists"
    USER_NOT_FOUND = "4001", "User not found"
    USER_FORBIDDEN = "4003", "Access Denied"


class UserException(BaseAppException):
    """user exception"""

    class UserExistsException(BaseAppException):
        code: str = UserExceptionInfo.USER_ALREADY_EXISTS.code
        error: str = UserExceptionInfo.USER_ALREADY_EXISTS.error

    class UserNotFoundException(BaseAppException):
        code: str = UserExceptionInfo.USER_NOT_FOUND.code
        error: str = UserExceptionInfo.USER_NOT_FOUND.error

    class UserForbiddenException(BaseAppException):
        code: str = UserExceptionInfo.USER_FORBIDDEN.code
        error: str = UserExceptionInfo.USER_FORBIDDEN.error
