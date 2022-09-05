# ./backend/src/routers/v1/notes.py

from fastapi import APIRouter, Depends

import src.services.notes as note_services
from src.internal.auth.jwthandler import get_current_user
from src.schemas.users import UserOutSchema
from src.schemas.notes import NoteInSchema, NotesOutSchema
from src.schemas.base import Status


router = APIRouter()


@router.get(
    "/list",
    description="Получение списка заметок пользователя",
    response_model=list[NotesOutSchema],
)
async def list_notes(current_user: UserOutSchema = Depends(get_current_user)):
    return await note_services.get_note_list(author_id=current_user.id)


@router.post(
    "/add",
    description="Добавить заметку",
    response_model=NotesOutSchema
)
async def add_note(note: NoteInSchema, current_user: UserOutSchema = Depends(get_current_user)) -> NotesOutSchema:
    return await note_services.add_note(author_id=current_user.id, note=note)


@router.get(
    "/get/{note_id}",
    description="Получить информацию о заметке",
    response_model=NotesOutSchema,
    dependencies=[Depends(get_current_user)]
)
async def get_note(note_id: int):
    return await note_services.get_note(note_id)


@router.delete(
    "/delete/{note_id}",
    description="Удалить заметку",
    response_model=Status,
    dependencies=[Depends(get_current_user)]
)
async def delete_note(note_id: int) -> Status:
    return await note_services.delete_note(note_id)
