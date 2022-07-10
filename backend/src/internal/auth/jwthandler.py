
from os import getenv
from typing import Optional
from datetime import timedelta, datetime
from jose import jwt


JWT_SECRET_KEY = getenv("SECRET_KEY", "test123")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRED_MINUTES = 30
DEFAULT_TOKEN_EXPIRED_MINUTES = 15


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
