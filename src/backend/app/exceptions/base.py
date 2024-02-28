from enum import Enum


class ExceptionEnum(Enum):
    @property
    def code(self):
        return self.value[0]

    @property
    def error(self):
        return self.value[1]


class BaseExceptionInfo(ExceptionEnum):
    BASE_ERROR = "0000", "Something went wrong ..."
    BASE_AUTH_ERROR = "1000", "Unauthorized"
    BASE_CLIENT_ERROR = "2000", "Something went wrong ..."
    BASE_FORBIDDEN_ERROR = "3000", "Forbidden!"
    BASE_NOT_FOUND_ERROR = "4000", "Not Found!"
    BASE_CONFLICT_ERROR = "5000", "Conflict!"


class BaseAppException(Exception):
    code: str = BaseExceptionInfo.BASE_ERROR.code
    error: str = BaseExceptionInfo.BASE_ERROR.error
    detail: str | None = None

    def __init__(self, detail: str | None = None):
        super().__init__(detail)
        self.detail = detail


class BaseAuthException(BaseAppException):
    code: str = BaseExceptionInfo.BASE_AUTH_ERROR.code
    error: str = BaseExceptionInfo.BASE_AUTH_ERROR.error


class BaseForbiddenException(BaseAppException):
    code: str = BaseExceptionInfo.BASE_FORBIDDEN_ERROR.code
    error: str = BaseExceptionInfo.BASE_FORBIDDEN_ERROR.error


class BaseNotFoundException(BaseAppException):
    code: str = BaseExceptionInfo.BASE_NOT_FOUND_ERROR.code
    error: str = BaseExceptionInfo.BASE_NOT_FOUND_ERROR.error


class BaseConflictException(BaseAppException):
    code: str = BaseExceptionInfo.BASE_CONFLICT_ERROR.code
    error: str = BaseExceptionInfo.BASE_CONFLICT_ERROR.error
