# ./backend/src/services/users.py

from passlib.context import CryptContext
from asyncpg.exceptions import UniqueViolationError
from sqlalchemy.sql import insert, select
from fastapi.exceptions import HTTPException
from fastapi import status

from src.schemas.users import UserInSchema, UserOutSchema, UserDatabaseSchema
from src.models.database import database
from src.models.users import User

pwd_context = CryptContext(schemes=["bcrypt"])


async def create_user(user: UserInSchema) -> UserOutSchema:
    user.password = pwd_context.encrypt(user.password)
    query = insert(User).values(user.dict(exclude_none=True)).returning(User)

    try:
        user_obj = await database.fetch_one(query)
    except UniqueViolationError:
        raise HTTPException(status_code=409, detail="username already exists")

    return UserOutSchema.from_orm(user_obj)


async def get_user(username: str) -> UserDatabaseSchema:
    user_obj = None
    query = select(User).where(User.username == username)

    try:
        user_obj = await database.fetch_one(query)
    except Exception as e:
        print("\n\n")
        print(e)
        print("\n\n")

    if user_obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return UserDatabaseSchema.from_orm(user_obj)
