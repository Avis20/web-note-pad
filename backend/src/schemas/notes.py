# ./backend/src/schemas/notes.py

from pydantic import BaseModel
from src.schemas.users import UserOutSchema

class NotesOutSchema(BaseModel):
    id: int
    title: str
    content: str | None = None
    author_id: int

    # author: UserOutSchema

    class Config:
        orm_mode = True


class NoteInSchema(BaseModel):
    title: str
    content: str | None = None
