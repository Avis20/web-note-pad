import logging
from fastapi import APIRouter, status

from app.dependencies import UserServiceDep
from app.schemas.request.user import UserLoginSchema, UserRegistrationSchema
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
    return await user_service.create_user(request_user)


@router.post("/login", summary="Авторизация пользователя")
async def _login(
    request_user: UserLoginSchema,
    user_service: UserServiceDep,
):
    logger.debug(f"Login: {request_user.safe_data()}")
    await user_service.user_login(request_user)
