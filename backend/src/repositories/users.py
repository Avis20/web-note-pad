from dataclasses import dataclass
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status

from src.models.users import Users
from src.repositories.base import BaseCRUD


@dataclass
class UserRepository(BaseCRUD):
    db_session: Session
    model = Users

    def get_user_by_name(self, username: str):
        user_db = self.find(username=username)
        if user_db is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with '{username}' not found",
            )
        return user_db
