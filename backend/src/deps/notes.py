from fastapi import Depends
from sqlalchemy.orm import Session

from src.models.database import db_session

from src.repositories.notes import NoteRepository
from src.services.notes import NoteService


def get_note_service(db_session: Session = Depends(db_session)) -> NoteService:
    repository = NoteRepository(db_session)
    return NoteService(repository)
