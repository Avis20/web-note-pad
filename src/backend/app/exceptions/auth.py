from app.exceptions.base import BaseAuthException


class AuthException(BaseAuthException):
    class TokenEncodeException(BaseAuthException):
        pass

    class TokenDecodeException(BaseAuthException):
        pass

    class TokenExpiredException(BaseAuthException):
        pass
