# ./backend/src/schemas/token.py

from typing import Optional
from pydantic import BaseModel


class TokenData(BaseModel):
    """Вытащим имя пользователя из токена"""

    username: Optional[str] = None


class Status(BaseModel):
    """???"""

    message = str
