import logging

from app.dependencies import UserServiceDep
from app.schemas.request.user import UserRegistrationSchema
from fastapi import APIRouter, status

router = APIRouter(prefix="/user")

logger = logging.getLogger()


@router.post(
    "/registration",
    summary="Регистрация",
    description="Регистрация пользователей в системе",
    status_code=status.HTTP_201_CREATED,
)
async def _registration(
    request_user: UserRegistrationSchema,
    user_service: UserServiceDep,
):
    logger.debug(f"Registration: {request_user.safe_data()}")
    await user_service.create_user()
