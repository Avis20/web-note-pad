# ./backend/src/auth/jwthandler.py

import os
from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends, Request, HTTPException
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from tortoise.exceptions import DoesNotExist
from jose import JWTError, jwt

from src.database.models import Users
from src.schemas.users import UserOutSchema
from src.schemas.token import TokenData


JWT_SECRET_KEY = os.getenv("SECRET_KEY", "test123")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRED_MINUTES = 30
DEFAULT_TOKEN_EXPIRED_MINUTES = 15

# Специальный класс для авторизации
class OAuth2PasswordBearerCookie(OAuth2):
    def __init__(
        self,
        token_url: str,
        scheme_name: str = None,
        scopes: dict = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": token_url, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)
        # Зачем scopes? Зачем flows?

    async def __call__(self, request: Request) -> Optional[str]:
        # Получаем строку "Bearer: токен"
        auth: str = request.cookies.get("Authorization")
        print("auth =", auth)
        # Отделяем схему (Bearer) от параметров (токена)
        scheme, param = get_authorization_scheme_param(auth)

        if not auth or scheme.lower() != "bearer:":
            if self.auto_error:
                raise HTTPException(
                    status_code=401,
                    detail="Not authenticated",
                    headers={"WWW-Authenticated": "Bearer"},
                )
            else:
                return None

        return param


# Зачем token_url= ?
security = OAuth2PasswordBearerCookie(token_url="/login")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=DEFAULT_TOKEN_EXPIRED_MINUTES)

    to_encode.update({"exp": int(expire.timestamp())})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)
    print(f"\nJWT TOKEN = {encoded_jwt}\n")
    return encoded_jwt


async def get_current_user(token: str = Depends(security)):
    cred_except = HTTPException(
        status_code=401,
        detail="Not Authenticated",
        headers={"WWW-Authenticated": "Bearer"},
    )

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        print(type(payload))
        username: str = payload.get("sub")
        if username is None:
            raise cred_except
        # Зачем TokenData ?
        token_data = TokenData(username=username)
    except JWTError as e:
        print(e)
        raise cred_except

    try:
        db_user = await UserOutSchema.from_queryset_single(
            Users.get(username=token_data.username)
        )
    except DoesNotExist:
        raise cred_except

    return db_user
