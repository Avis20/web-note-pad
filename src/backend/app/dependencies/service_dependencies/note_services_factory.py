from typing import Annotated
from fastapi import Depends

from app.services.notes import NoteService
from app.dependencies import NoteUoWDep


def create_note_service(note_uow: NoteUoWDep):
    return NoteService(note_uow)


NoteServiceDep = Annotated[NoteService, Depends(create_note_service)]
