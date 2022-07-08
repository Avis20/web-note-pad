# ./backend/src/services/users.py

from passlib.context import CryptContext
from asyncpg.exceptions import UniqueViolationError
from fastapi.exceptions import HTTPException
from src.schemas.users import UserInSchema, UserOutSchema
from src.models.database import database
from sqlalchemy.sql import insert, select
from src.models.users import User

pwd_context = CryptContext(schemes=["bcrypt"])


async def create_user(user: UserInSchema) -> UserOutSchema:
    user.password = pwd_context.encrypt(user.password)
    query = insert(User).values(**user.dict(exclude_none=True))

    try:
        user_obj = await database.fetch_one(query)
    except UniqueViolationError:
        raise HTTPException(status_code=409, detail="username already exists")

    print("\n\n user_obj")
    print(type(user_obj))
    print("\n\n")
    return UserOutSchema.from_orm(user_obj)


async def get_user(user_id: int):
    query = select(User).where(User.id == user_id)
    user = await database.fetch_one(query=query)
    return user
