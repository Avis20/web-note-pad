from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.schemas.response.base import ResponseSchema


class UserItemResponseSchema(BaseModel):
    id: UUID
    username: str
    full_name: str | None = None
    created_at: datetime
    updated_at: datetime


class UserResponseSchema(ResponseSchema):
    item: UserItemResponseSchema
