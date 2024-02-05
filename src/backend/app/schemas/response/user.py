from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserResponseSchema(BaseModel):
    id: UUID
    username: str
    full_name: str
    created_at: datetime
    updated_at: datetime
