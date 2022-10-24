# ./backend/src/services/users.py

from passlib.context import CryptContext
from psycopg2.errors import UniqueViolation
from sqlalchemy.orm import Session

from sqlalchemy.sql import insert, delete, select
from fastapi.exceptions import HTTPException
from fastapi import status

from src.schemas.users import UserInSchema, UserOutSchema, UserDatabaseSchema

# from src.models.database import database
from src.models.users import Users
from src.schemas.base import Status

pwd_context = CryptContext(schemes=["bcrypt"])


def create_user(user: UserInSchema, db_session: Session) -> UserOutSchema:
    user.password = pwd_context.encrypt(user.password)
    user = Users(**user.dict(exclude_none=True))

    try:
        user_obj = user.save(db_session)
    except UniqueViolation:
        raise HTTPException(status_code=409, detail="Username already exists")

    return UserOutSchema.from_orm(user_obj)


def get_user(username: str, db_session: Session) -> UserDatabaseSchema:
    user_obj = None

    try:
        user_obj = Users.find(db_session, field="username", value=username)
    except Exception as e:
        print("\n\n")
        print(e)
        print("\n\n")

    if user_obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return UserDatabaseSchema.from_orm(user_obj)


def delete_user(
    user_id: int, current_user: UserDatabaseSchema, db_session: Session
) -> Status:

    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="access denied"
        )

    try:
        Users.delete(db_session, current_user.id)
    except Exception as e:
        print("\n\n")
        print(e)
        print("\n\n")

    return Status(message="success")
