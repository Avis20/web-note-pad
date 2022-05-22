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


async def delete_user(user_id, current_user):
    cred_except = HTTPException(status_code=404, detail=f"User {user_id} not found")
    try:
        db_user = await UserOutSchema.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist:
        raise cred_except

    if db_user.id == current_user.id:
        # delete_count = await Users.filter(id=user_id).delete()
        delete_count = 1
        print("delete_count", delete_count)
        print(type(delete_count))
        if not delete_count:
            raise cred_except
        else:
            # По идеи можно было бы вернуть строку, но pydantic ругается что ему нужен словарь
            return {"message": f"User {user_id} is delete"}

    raise cred_except
