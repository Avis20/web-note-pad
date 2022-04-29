# ./backend/src/routes/users.py

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

import src.crud.users as crud
from src.auth.users import validate_user
from src.schemas.users import UserInSchema, UserOutSchema


router = APIRouter()

@router.post('/register', response_model=UserOutSchema)
async def create_user(user: UserInSchema) -> UserOutSchema:
    return await crud.create_user(user)


@router.post('/login')
async def login_user(user: OAuth2PasswordRequestForm = Depends()):
    user = await validate_user(user)

# @router.delete(
#     '/user/{user_id}',
# )
# async def delete_user(user_id: int, current_user: UserOutSchema = Depends())