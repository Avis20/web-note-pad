
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.schemas.users import UserDatabaseSchema
from src.database.models import Users

async def get_user(username: str):
    # зачем from_queryset_single?
    return await UserDatabaseSchema.from_queryset_single(Users.get(username=username))

async def validate_user(user: OAuth2PasswordRequestForm = Depends()):
    db_user = await get_user(user.username)
