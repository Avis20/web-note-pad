# ./backend/schemas/users.py

from pydantic import BaseModel
from datetime import datetime

class UserInSchema(BaseModel):
    username: str
    full_name: str
    password: str

class UserOutSchema(BaseModel):
    id: int
    username: str
    full_name: str
    created_at: datetime
    modified_at: datetime
