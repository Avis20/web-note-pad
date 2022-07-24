from os import getenv
from typing import Optional
from datetime import timedelta, datetime

from fastapi import Depends, Request, HTTPException
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.models import OAuthFlow as OAuthFlowsModel
from jose import JWTError, jwt

from src.services.users import get_user
from src.schemas.token import TokenData
from src.schemas.users import UserDatabaseSchema

JWT_SECRET_KEY = getenv("SECRET_KEY", "test123")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRED_MINUTES = 30
DEFAULT_TOKEN_EXPIRED_MINUTES = 15


class OAuth2PasswordBearerCookie(OAuth2):
    """Специальный класс для авторизации"""

    def __init__(
        self,
        token_url: str,
        scheme_name: str | None = None,
        scopes: dict | None = None,
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


async def get_current_user(token: str = Depends(security)) -> UserDatabaseSchema:
    print(f"\nInput JWT TOKEN = {token}\n")
    auth_except = HTTPException(
        status_code=401,
        detail="Not Authenticated",
        headers={"WWW-Authenticated": "Bearer"},
    )

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        print(f"payload: type={type(payload)}; {payload}")
        username = payload.get("sub")
        if username is None:
            raise auth_except
    except JWTError as e:
        print(e)
        raise auth_except

    db_user = await get_user(username=username)
    return db_user
