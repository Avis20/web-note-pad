from dataclasses import dataclass
from sqlalchemy.orm import Session

from src.models.notes import Notes

from src.repositories.base import BaseCRUD


@dataclass
class NoteRepository(BaseCRUD):
    db_session: Session
    model = Notes

    def get_list_by_author_id(self, author_id: int):
        notes = self.get_list(author_id=author_id)
        return notes

    def get_by_id(self, note_id: int) -> Notes:
        return Notes.find(self.db_session, id=note_id)
