from typing import Annotated
from fastapi import Depends
from app.dependencies.common import get_settings

from app.services.auth import AuthService
from app.settings import Settings


def create_auth_service(
    settings: Annotated[Settings, Depends(get_settings)],
):
    return AuthService(jwt_secret_key=settings.project.jwt_secret_key)


AuthServiceDep = Annotated[AuthService, Depends(create_auth_service)]
