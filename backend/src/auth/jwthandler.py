# ./backend/src/auth/jwthandler.py

from datetime import timedelta
from typing import Optional


ACCESS_TOKEN_EXPIRED_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    # if expires_delta:
    #     expire = 
    pass
