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


class BaseAppException(Exception):
    """Base Exception"""

    code: str = BaseExceptionInfo.BASE_ERROR.code
    error: str = BaseExceptionInfo.BASE_ERROR.error
    detail: str | None = None

    def __init__(self, detail: str | None = None):
        super().__init__(detail)
        self.detail = detail


class BaseAuthException(BaseAppException):
    """Base Token Exception"""

    code: str = BaseExceptionInfo.BASE_AUTH_ERROR.code
    error: str = BaseExceptionInfo.BASE_AUTH_ERROR.error
