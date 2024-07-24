import logging
from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from app.constants.auth import EXPIRE_ACCESS_TOKEN

from app.dependencies import UserServiceDep, AuthServiceDep
from app.dependencies.auth import get_current_user
from app.dto.users import UserDTO
from app.schemas.request.users import UserLoginSchema, UserRegistrationSchema
from app.schemas.response.auth import TokenResponseSchema
from app.schemas.response.base import ResponseSchema
from app.schemas.response.users import UserItemResponseSchema, UserResponseSchema

router = APIRouter(prefix="/user", tags=["User"])

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
    if user:
        return UserResponseSchema(
            success=1,
            item=UserItemResponseSchema(**user.as_dict()),
            params=request_user.safe_data(),
        )


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
    response = JSONResponse({"success": 1, "item": tokens.as_dict(), "params": request_user.safe_data()})
    response.set_cookie(
        "Authorization",
        value=f"Bearer {tokens.access_token}",
        httponly=True,
        max_age=1800,
        expires=EXPIRE_ACCESS_TOKEN,
        secure=False,
    )
    return response


@router.get(
    "/get",
    summary="Данные пользователя",
    description="Получение данных авторизованного пользователя",
    response_model=UserResponseSchema,
)
async def _user_get(
    user_dto: Annotated[UserDTO, Depends(get_current_user)],
):
    return UserResponseSchema(success=1, item=UserItemResponseSchema(**user_dto.as_dict()))


@router.delete(
    "/delete",
    summary="Удаление пользователя",
    description="Удаление данных о пользователе",
    response_model=ResponseSchema,
)
async def _user_delete(
    user_dto: Annotated[UserDTO, Depends(get_current_user)],
    user_service: UserServiceDep,
):
    await user_service.delete_user(user_id=user_dto.id)
    return ResponseSchema(success=1)
