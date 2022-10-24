# ./backend/src/routers/v1/users.py

from datetime import timedelta

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from src.models.database import db_session

import src.services.users as users_services
from src.schemas.users import UserInSchema, UserOutSchema, UserDatabaseSchema
from src.schemas.base import Status, LogginSchema
from src.internal.auth.users import validate_user
from src.internal.auth.jwthandler import (
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRED_MINUTES,
)

router = APIRouter()


@router.post(
    "/register",
    response_model=UserOutSchema,
    description="Регистрация нового пользователя",
)
def create_user(
    user: UserInSchema, db_session: Session = Depends(db_session)
) -> UserOutSchema:
    return users_services.create_user(user, db_session)


@router.post("/login", description="Логин", response_model=LogginSchema)
def login_user(
    user: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(db_session),
):
    user = validate_user(user, db_session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    access_token_expired = timedelta(minutes=ACCESS_TOKEN_EXPIRED_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expired
    )
    token = access_token
    response = JSONResponse(LogginSchema().dict())
    response.set_cookie(
        "Authorization",
        value=f"Bearer: {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        secure=False,
    )
    return response


@router.get(
    "/info",
    response_model=UserOutSchema,
    description="Получение информации о текущем пользователе",
)
def user_info(current_user: UserOutSchema = Depends(get_current_user)):
    return current_user


@router.delete(
    "/delete/{user_id}",
    response_model=Status,
)
def user_delete(
    user_id: int,
    current_user: UserDatabaseSchema = Depends(get_current_user),
    db_session: Session = Depends(db_session),
) -> Status:
    return users_services.delete_user(user_id, current_user, db_session)
