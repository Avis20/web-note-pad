from app.exceptions.base import BaseAppException


class AuthException(BaseAppException):
    class TokenEncodeException(BaseAppException):
        pass
