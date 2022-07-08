# ./backend/src/routers/users.py


from fastapi import APIRouter
from src.schemas.users import UserInSchema, UserOutSchema
import src.services.users as users_services

router = APIRouter()


@router.post(
    "/register",
    response_model=UserOutSchema,
    description="Регистрация нового пользователя",
)
async def create_user(user: UserInSchema) -> UserOutSchema:
    return await users_services.create_user(user)


@router.get(
    "/user/info",
    response_model=UserOutSchema,
)
async def user_info(user_id: int) -> UserOutSchema:
    return await users_services.get_user(user_id)
