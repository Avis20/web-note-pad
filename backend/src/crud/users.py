# ./backend/src/crud/users.py

from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from passlib.context import CryptContext

from src.database.models import Users
from src.schemas.users import UserInSchema, UserOutSchema

pwd_context = CryptContext(schemes=["bcrypt"])


async def create_user(user: UserInSchema) -> UserOutSchema:
    """
    Добавить пользователя в БД

    Args:
        user (UserInSchema): _description_

    Returns:
        UserOutSchema: _description_
    """

    user.password = pwd_context.encrypt(user.password)
    try:
        # exclude_unset - исключить null значения
        user_obj = await Users.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(status_code=409, detail="username already exists")

    return await UserOutSchema.from_tortoise_orm(user_obj)
