# ./backend/schemas/users.py

from pydantic import BaseModel


class UserInSchema(BaseModel):
    username: str
    full_name: str | None = None
    password: str


class UserOutSchema(BaseModel):
    id: int
    username: str
    full_name: str | None = None

    class Config:
        orm_mode = True


class UserDatabaseSchema(BaseModel):
    id: int
    username: str
    full_name: str | None = None
    password: str

    class Config:
        orm_mode = True
