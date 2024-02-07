import logging

from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.exceptions import base as app_exceptions
from app.exceptions import user as user_exceptions

logger = logging.getLogger(__name__)


async def application_exception_handler(request: Request, exc: app_exceptions.BaseAppException):
    answer = {
        "code": exc.code,
        "error": exc.error,
        "detail": exc.detail,
    }
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    if isinstance(exc, app_exceptions.BaseAuthException):
        status_code = status.HTTP_401_UNAUTHORIZED
    elif isinstance(exc, user_exceptions.UserException.UserExistsException):
        status_code = status.HTTP_409_CONFLICT
    elif isinstance(exc, user_exceptions.UserException.UserForbiddenException):
        status_code = status.HTTP_403_FORBIDDEN

    logger.exception(exc, exc_info=exc)

    return JSONResponse(status_code=status_code, content=jsonable_encoder(answer))
