from pydantic import BaseModel

from app.schemas.request.base import PaginationRequestSchema


class NoteCreateSchema(BaseModel):
    title: str
    content: str


class NoteUpdateSchema(BaseModel):
    title: str | None = None
    content: str | None = None


class NoteListSchema(PaginationRequestSchema):
    pass
