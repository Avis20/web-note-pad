from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.schemas.response.base import ResponseSchema
from app.schemas.response.users import UserItemResponseSchema


class NoteItemResponseSchema(BaseModel):
    id: UUID
    title: str
    content: str | None
    author_id: UUID
    created_at: datetime
    updated_at: datetime
    author: UserItemResponseSchema


class NoteResponseSchema(ResponseSchema):
    item: NoteItemResponseSchema


class NoteListResponseSchema(ResponseSchema):
    list: list[NoteItemResponseSchema]
