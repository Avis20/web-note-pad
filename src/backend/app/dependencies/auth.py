import logging

from typing import Annotated
from fastapi import Depends, Request
from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowPassword
from fastapi.security.utils import get_authorization_scheme_param

from app.dependencies import AuthServiceDep, UserServiceDep
from app.dto.auth import AuthDataDTO
from app.dto.users import UserDTO
from app.exceptions.auth import AuthException


logger = logging.getLogger(__name__)


class OAuth2PasswordBearerCookie(OAuth2):
    def __init__(
        self,
        token_url: str,
        scheme_name: str | None = None,
        scopes: dict | None = None,
        auto_error: bool = False,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password=OAuthFlowPassword(tokenUrl=token_url, scopes=scopes))
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> str | None:
        authorization: str = request.cookies.get("Authorization", "")
        scheme, access_token = get_authorization_scheme_param(authorization)
        if not access_token or scheme.lower() != 'bearer':
            if self.auto_error:
                raise AuthException("Token is required!")
            return None
        return access_token


get_cookie_token = OAuth2PasswordBearerCookie(token_url="/login")  # noqa


async def get_current_user(
    access_token: Annotated[str, Depends(get_cookie_token)],
    auth_service: AuthServiceDep,
    user_service: UserServiceDep,
) -> UserDTO:
    if not access_token:
        raise AuthException("Token is required!")

    auth_data: AuthDataDTO = await auth_service.extract_auth_data(access_token)
    user = await user_service.get_user_by_id(user_id=auth_data.user_id)
    return user
