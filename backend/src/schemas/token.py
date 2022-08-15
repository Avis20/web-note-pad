# ./backend/src/schemas/token.py

from pydantic import BaseModel

class TokenData(BaseModel):
    username: str | None = None
