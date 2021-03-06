# ./backend/src/services/users.py

from passlib.context import CryptContext
from psycopg2.errors import UniqueViolation
from sqlalchemy.sql import insert, delete, select
from fastapi.exceptions import HTTPException
from fastapi import status

from src.schemas.users import UserInSchema, UserOutSchema, UserDatabaseSchema
from src.models.database import database
from src.models.users import Users
from src.schemas.base import Status

pwd_context = CryptContext(schemes=["bcrypt"])


async def create_user(user: UserInSchema) -> UserOutSchema:
    user.password = pwd_context.encrypt(user.password)
    query = insert(Users).values(user.dict(exclude_none=True)).returning(Users)

    try:
        user_obj = await database.fetch_one(query)
    except UniqueViolation:
        raise HTTPException(status_code=409, detail="Username already exists")

    return UserOutSchema.from_orm(user_obj)


async def get_user(username: str) -> UserDatabaseSchema:
    user_obj = None
    query = select(Users).where(Users.username == username)

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


async def delete_user(user_id: int, current_user: UserDatabaseSchema) -> Status:

    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="access denied"
        )

    query = delete(Users).where(Users.id == current_user.id)

    try:
        await database.execute(query)
    except Exception as e:
        print("\n\n")
        print(e)
        print("\n\n")

    return Status(message="success")
