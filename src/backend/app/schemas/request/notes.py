from pydantic import BaseModel

from app.schemas.request.base import PaginationRequestSchema


class NoteCreateSchema(BaseModel):
    content: str


class NoteUpdateSchema(BaseModel):
    content: str


class NoteListSchema(PaginationRequestSchema):
    pass
