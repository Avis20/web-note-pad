# ./backend/src/auth/jwthandler.py

import os
from datetime import timedelta, datetime
from typing import Optional
from fastapi import Depends
from fastapi.security import OAuth2
from jose import JWTError, jwt

JWT_SECRET_KEY = os.getenv("SECRET_KEY", "test123")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRED_MINUTES = 30
DEFAULT_TOKEN_EXPIRED_MINUTES = 15


class OAuth2PasswordBearerCookie(OAuth2):
    def __init__(self, token_url):
        pass


security = OAuth2PasswordBearerCookie(token_url="/login")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=DEFAULT_TOKEN_EXPIRED_MINUTES)

    to_encode.update({"expire": str(expire)})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)
    print(f"\nJWT TOKEN = {encoded_jwt}\n")
    return encoded_jwt


async def get_current_user(token: Depends(security)):
    pass
