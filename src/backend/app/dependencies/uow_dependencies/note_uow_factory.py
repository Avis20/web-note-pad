from typing import Annotated
from fastapi import Depends

from app.dependencies.clients.db_session import SessionMakerDep
from app.uow.notes import INoteUoW, NoteUoW


def create_note_uow(session_maker: SessionMakerDep):
    return NoteUoW(session_maker)


NoteUoWDep = Annotated[INoteUoW, Depends(create_note_uow)]
