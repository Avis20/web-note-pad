from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy import insert, select, delete, update
from app.dto.base import PaginationBaseDTO

from app.dto.notes import NoteCreateDTO, NoteDTO, NoteUpdateDTO
from app.repositories.base import SQLAlchemyRepository
from app.models.notes import Note


class INoteRepository(ABC):
    @abstractmethod
    async def create_note(self, note_data: NoteCreateDTO) -> NoteDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def get_note_by_user(self, note_id: UUID, user_id: UUID) -> NoteDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def update_note_by_user(self, note_update_dto: NoteUpdateDTO) -> NoteDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def delete_note_by_user(self, note_id: UUID, user_id: UUID) -> NoteDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def note_list_by_user(self, user_id: UUID, pagination_dto: PaginationBaseDTO) -> list[NoteDTO]:
        raise NotImplementedError


class NoteRepository(INoteRepository, SQLAlchemyRepository):
    async def update_note_by_user(self, note_update_dto: NoteUpdateDTO) -> NoteDTO | None:
        note_dto = await self.get_note_by_user(note_id=note_update_dto.id, user_id=note_update_dto.author_id)
        if not note_dto:
            return None
        data = note_update_dto.as_dict(exclude=['id', 'author_id'])
        stmt = update(Note).values(data).returning(Note)
        result = await self._session.execute(stmt)
        if note := result.scalar():
            return NoteDTO.model_to_dto(note)
        return None

    async def note_list_by_user(self, user_id: UUID, pagination_dto: PaginationBaseDTO) -> list[NoteDTO]:
        stmt = select(Note).filter_by(author_id=user_id).limit(pagination_dto.limit).offset(pagination_dto.offset)
        result = await self._session.execute(stmt)
        if notes := result.scalars():
            return [NoteDTO.model_to_dto(note) for note in notes]
        return []

    async def create_note(self, note_data: NoteCreateDTO) -> NoteDTO | None:
        stmt = insert(Note).values(note_data.as_dict()).returning(Note)
        result = await self._session.execute(stmt)
        if note := result.scalar():
            return NoteDTO.model_to_dto(note)
        return None

    async def get_note_by_user(self, note_id: UUID, user_id: UUID) -> NoteDTO | None:
        stmt = select(Note).filter_by(
            id=note_id,
            author_id=user_id,
        )
        result = await self._session.execute(stmt)
        if note := result.scalar():
            return NoteDTO.model_to_dto(note)
        return None

    async def delete_note_by_user(self, note_id: UUID, user_id: UUID) -> NoteDTO | None:
        note_dto = await self.get_note_by_user(note_id=note_id, user_id=user_id)
        if not note_dto:
            return None

        stmt = delete(Note).filter_by(
            id=note_id,
            author_id=user_id,
        )
        await self._session.execute(stmt)
        return note_dto
