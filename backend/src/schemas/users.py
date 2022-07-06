# ./backend/schemas/users.py

from pydantic import BaseModel
from datetime import datetime


class UserInSchema(BaseModel):
    username: str
    full_name: str | None = None
    password: str


class UserOutSchema(BaseModel):
    id: int
    username: str
    full_name: str
    created_at: datetime
    modified_at: datetime

    class Config:
        orm_mode = True
