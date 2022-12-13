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

# from src.internal.auth.users import validate_user
from src.internal.auth.jwthandler import (
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRED_MINUTES,
)

from src.deps.users import UserService, get_user_service

router = APIRouter()


@router.post(
    "/register",
    response_model=UserOutSchema,
    description="Регистрация нового пользователя",
)
def create_user(
    user: UserInSchema,
    user_service: UserService = Depends(get_user_service),
) -> UserOutSchema:
    return user_service.create_user(user)


@router.post("/login", description="Логин", response_model=LogginSchema)
def login_user(
    user: OAuth2PasswordRequestForm = Depends(),
    user_service: UserService = Depends(get_user_service),
):
    user = user_service.validate_user(user)

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
    user_service: UserService = Depends(get_user_service),
) -> Status:
    return user_service.delete_user(user_id, current_user)
