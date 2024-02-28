import logging
from typing import Annotated
from fastapi import APIRouter, Depends, status

from app.dependencies import UserServiceDep, AuthServiceDep
from app.dependencies.auth import get_current_user
from app.dto.user import UserDTO
from app.schemas.request.user import UserLoginSchema, UserRegistrationSchema
from app.schemas.response.auth import TokenResponseSchema
from app.schemas.response.base import ResponseSchema
from app.schemas.response.user import UserResponseSchema

router = APIRouter(prefix="/user")

logger = logging.getLogger()


@router.post(
    "/registration",
    summary="Регистрация",
    description="Регистрация пользователей в системе",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseSchema,
)
async def _registration(
    request_user: UserRegistrationSchema,
    user_service: UserServiceDep,
):
    logger.debug(f"Registration: {request_user.safe_data()}")
    user = await user_service.create_user(request_user)
    return {"success": 1, "item": user, "params": request_user.safe_data()}


@router.post(
    "/login",
    summary="Логин",
    description="Авторизация пользователя",
    response_model=TokenResponseSchema,
)
async def _login(
    request_user: UserLoginSchema,
    user_service: UserServiceDep,
    auth_service: AuthServiceDep,
):
    logger.debug(f"Login: {request_user.safe_data()}")
    user = await user_service.user_login(request_user)
    tokens = await auth_service.create_token_pair(user_id=user.id)
    # TODO: set_cookie
    return {"success": 1, "item": tokens, "params": request_user.safe_data()}


@router.get(
    "/get",
    summary="Данные пользователя",
    description="Получение данных авторизованного пользователя",
    response_model=UserResponseSchema,
)
async def _user_get(
    user: Annotated[UserDTO, Depends(get_current_user)],
):
    return {"success": 1, "item": user}


@router.delete(
    "/delete",
    summary="Удаление пользователя",
    description="Удаление данных о пользователе",
    response_model=ResponseSchema,
)
async def _user_delete(
    user: Annotated[UserDTO, Depends(get_current_user)],
    user_service: UserServiceDep,
):
    await user_service.delete_user(user_id=user.id)
    return {"success": 1}
