from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.dto.base import DTO
from app.dto.users import UserDTO


@dataclass
class NoteCreateDTO(DTO):
    title: str
    content: str
    author_id: UUID


@dataclass
class NoteUpdateDTO(DTO):
    title: str | None = None
    content: str | None = None


@dataclass
class NoteDTO(DTO):
    id: UUID
    title: str
    content: str
    author_id: UUID
    created_at: datetime
    updated_at: datetime
    author: UserDTO
