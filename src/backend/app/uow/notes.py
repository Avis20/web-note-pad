from __future__ import annotations

from app.repositories.notes import INoteRepository, NoteRepository
from app.uow.base import SQLAlchemyUoW, UnitOfWorkABC


class INoteUoW(UnitOfWorkABC):
    note_repo: INoteRepository


class NoteUoW(SQLAlchemyUoW, INoteUoW):
    async def __aenter__(self) -> NoteUoW:
        await super().__aenter__()
        self.note_repo = NoteRepository(self.session)
        return self
