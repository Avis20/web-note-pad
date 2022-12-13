# ./backend/src/services/notes.py

from fastapi import HTTPException
from dataclasses import dataclass

from src.schemas.notes import NoteInSchema, NotesOutSchema

from src.repositories.notes import NoteRepository
from src.models.notes import Notes
from src.schemas.base import Status


@dataclass
class NoteService:
    repository: NoteRepository

    def add_note(self, author_id: int, note: NoteInSchema) -> NotesOutSchema:
        note = Notes(**note.dict(exclude_none=True), author_id=author_id)
        note_db = self.repository.create(note)
        return NotesOutSchema.from_orm(note_db)

    def note_list(self, author_id: int) -> list[NotesOutSchema]:
        return self.repository.get_list_by_author_id(author_id)

    def get_author_note(self, author_id: int, note_id: int) -> NotesOutSchema:
        return self.repository.find(author_id=author_id, id=note_id)

    def delete_note(self, author_id: int, note_id: int):
        note_db = self.get_author_note(author_id, note_id)
        if not note_db:
            raise HTTPException(
                status_code=404,
                detail=f"Note with '{note_id}' for user '{author_id}' not found",
            )

        self.repository.delete(id=note_id)
        return Status(message="success")
