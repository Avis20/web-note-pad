# ./backend/src/schemas/notes.py

from pydantic import BaseModel

class NotesOutSchema(BaseModel):
    id: int
    title: str
    content: str | None = None

    class Config:
        orm_mode = True


class NoteInSchema(BaseModel):
    title: str
    content: str | None = None
