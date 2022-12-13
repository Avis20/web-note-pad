from fastapi import Depends
from sqlalchemy.orm import Session

from src.models.database import db_session

from src.repositories.users import UserRepository
from src.services.users import UserService


def get_user_service(db_session: Session = Depends(db_session)) -> UserService:
    repository = UserRepository(db_session)
    return UserService(repository)
