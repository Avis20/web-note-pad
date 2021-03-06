# ./backend/src/routes/users.py

from datetime import timedelta
from tortoise.contrib.fastapi import HTTPNotFoundError
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

import src.crud.users as crud
from src.auth.users import validate_user
from src.schemas.users import UserInSchema, UserOutSchema
from src.schemas.token import Status
from src.auth.jwthandler import (
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
async def create_user(user: UserInSchema) -> UserOutSchema:
    return await crud.create_user(user)


@router.post("/login", description="Логин")
async def login_user(user: OAuth2PasswordRequestForm = Depends()):
    user = await validate_user(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    access_token_expired = timedelta(minutes=ACCESS_TOKEN_EXPIRED_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expired
    )
    # Зачем jsonable_encoder?
    # token = jsonable_encoder(access_token)
    token = access_token
    content = {"message": "Loggined", "success": 1}
    response = JSONResponse(content)
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
    "/user/info",
    response_model=UserOutSchema,
    description="Получение информации о текущем (залогиненом) пользователе",
)
async def user_info(current_user: UserOutSchema = Depends(get_current_user)):
    return current_user


@router.delete(
    '/user/{user_id}',
    description="Удаление пользователя",
    response_model=Status,
    responses={"404": {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)]
)
async def delete_user(user_id: int, current_user: UserOutSchema = Depends(get_current_user)) -> Status:
    return await crud.delete_user(user_id, current_user)
