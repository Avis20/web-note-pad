# ./backend/src/services/users.py

from passlib.context import CryptContext
from psycopg2.errors import UniqueViolation

from dataclasses import dataclass

from src.repositories.users import UserRepository

from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status

from src.schemas.users import UserInSchema, UserOutSchema, UserDatabaseSchema

from src.models.users import Users
from src.schemas.base import Status

pwd_context = CryptContext(schemes=["bcrypt"])


@dataclass
class UserService:
    repository: UserRepository

    def create_user(self, user: UserInSchema) -> UserOutSchema:
        user.password = pwd_context.encrypt(user.password)
        user = Users(**user.dict(exclude_none=True))

        try:
            user_db = self.repository.create(user)
        except UniqueViolation:
            raise HTTPException(
                status_code=409, detail=f"User with '{user.username}' already exists"
            )

        return UserOutSchema.from_orm(user_db)

    def validate_user(self, user: OAuth2PasswordRequestForm):
        db_user = self.repository.get_user_by_name(user.username)

        # проверяем валидность пароля что в БД и что пришло в запросе
        if not self.verify_password(user.password, db_user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect"
            )
        return db_user

    def verify_password(self, plan_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plan_password, hashed_password)

    def delete_user(self, user_id: int, current_user: UserDatabaseSchema) -> Status:
        if current_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="access denied"
            )

        try:
            self.repository.delete(id=current_user.id)
        except Exception as e:
            print("\n\n")
            print(e)
            print("\n\n")

        return Status(message="success")
