from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.dto.base import DTO


@dataclass
class UserCreateDTO(DTO):
    username: str
    password: str
    full_name: str | None = None


@dataclass
class UserDTO(DTO):
    id: UUID
    username: str
    password: str
    created_at: datetime
    updated_at: datetime
    full_name: str | None = None

    def safe_data(self) -> dict:
        return self.as_dict(exclude=["password"])
