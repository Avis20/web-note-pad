from uuid import UUID

from pydantic import BaseModel

from app.schemas.response.base import ResponseSchema


class TokenItemResponseSchema(BaseModel):
    access_token: str
    refresh_token: UUID


class TokenResponseSchema(ResponseSchema):
    item: TokenItemResponseSchema
