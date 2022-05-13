# ./backend/src/auth/users.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from tortoise.exceptions import DoesNotExist
from passlib.context import CryptContext

from src.schemas.users import UserDatabaseSchema
from src.database.models import Users


async def get_user(username: str) -> UserDatabaseSchema:
    # зачем from_queryset_single?
    """
        user_db = await Users.get(username=username)
        print('\n\n')
        print(user_db)
        print(type(user_db))
        print(user_db.username)
        # >>> <Users>
        # >>> <class 'src.database.models.Users'>
        # >>> stri1ng11211111

        user_db = Users.get(username=username)
        user = await UserDatabaseSchema.from_queryset_single(user_db)
        print(user)
        print(type(user))
        print(user.username)
        print('\n\n')
        # >>> id=15 username='stri1ng11211111' full_name=None password='$2b$12$Rbb9hEbohqotZexABmAqDO5Z5m.wudfU3InAkv7CypkvNtkuiitK2'
        # >>> <class 'abc.User'>
        # >>> stri1ng11211111
    """
    return await UserDatabaseSchema.from_queryset_single(Users.get(username=username))


pwd_context = CryptContext(schemes=["bcrypt"])


def verify_password(plan_password, hashed_password):
    return pwd_context.verify(plan_password, hashed_password)


async def validate_user(
    user: OAuth2PasswordRequestForm = Depends(),
) -> UserDatabaseSchema:
    try:
        db_user = await get_user(user.username)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    # проверяем валидность пароля что в БД и что пришло в запросе
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect"
        )
    return db_user
