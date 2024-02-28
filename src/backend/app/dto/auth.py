from dataclasses import dataclass
from uuid import UUID

from app.dto.base import DTO


@dataclass
class TokenDTO(DTO):
    access_token: str
    refresh_token: UUID


@dataclass
class AuthDataDTO(DTO):
    user_id: UUID
