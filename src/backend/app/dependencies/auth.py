import logging

from typing import Annotated
from fastapi import Security
from fastapi.security import APIKeyHeader
from fastapi.security.utils import get_authorization_scheme_param

from app.dependencies import AuthServiceDep, UserServiceDep
from app.dto.auth import AuthDataDTO
from app.dto.user import UserDTO
from app.exceptions.auth import AuthException

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


logger = logging.getLogger(__name__)


async def get_current_user(
    token: Annotated[str, Security(api_key_header)],
    auth_service: AuthServiceDep,
    user_service: UserServiceDep,
) -> UserDTO:
    if not token:
        raise AuthException("Token is required!")

    _, access_token = get_authorization_scheme_param(token)
    auth_data: AuthDataDTO = await auth_service.extract_auth_data(access_token)
    user = await user_service.get_user_by_id(user_id=auth_data.user_id)
    return user
