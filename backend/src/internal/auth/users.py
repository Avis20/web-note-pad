# ./backend/src/internal/auth/users.py

from fastapi import status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from src.schemas.users import UserDatabaseSchema
from src.services.users import get_user
from src.models.database import db_session

pwd_context = CryptContext(schemes=["bcrypt"])


def verify_password(plan_password, hashed_password):
    return pwd_context.verify(plan_password, hashed_password)


def validate_user(
    user: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(db_session),
) -> UserDatabaseSchema:
    db_user = get_user(user.username, db_session)

    # проверяем валидность пароля что в БД и что пришло в запросе
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect"
        )
    return db_user
