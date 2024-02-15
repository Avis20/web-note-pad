from uuid import UUID

from pydantic import BaseModel


class TokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: UUID
