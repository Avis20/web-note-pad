from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.dto.base import DTO


@dataclass
class NoteCreateDTO(DTO):
    content: str
    author_id: UUID


@dataclass
class NoteUpdateDTO(DTO):
    id: UUID
    content: str
    author_id: UUID


@dataclass
class NoteDTO(DTO):
    id: UUID
    content: str
    author_id: UUID
    created_at: datetime
    updated_at: datetime
