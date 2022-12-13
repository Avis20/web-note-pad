# ./backend/src/routers/v1/notes.py

from fastapi import APIRouter, Depends


from src.services.notes import NoteService

from src.internal.auth.jwthandler import get_current_user
from src.schemas.users import UserDatabaseSchema, UserOutSchema
from src.schemas.notes import NoteInSchema, NotesOutSchema
from src.schemas.base import Status

from src.deps.notes import get_note_service


router = APIRouter()


@router.post("/add", description="Добавить заметку", response_model=NotesOutSchema)
def add_note(
    note: NoteInSchema,
    current_user: UserDatabaseSchema = Depends(get_current_user),
    note_service: NoteService = Depends(get_note_service),
) -> NotesOutSchema:
    return note_service.add_note(author_id=current_user.id, note=note)


@router.get(
    "/list",
    description="Получение списка заметок пользователя",
    response_model=list[NotesOutSchema],
)
def list_notes(
    current_user: UserOutSchema = Depends(get_current_user),
    note_service: NoteService = Depends(get_note_service),
) -> list[NotesOutSchema]:
    return note_service.note_list(author_id=current_user.id)


@router.get(
    "/get/{note_id}",
    description="Получить информацию о заметке",
    response_model=NotesOutSchema,
)
def get_note(
    note_id: int,
    current_user: UserOutSchema = Depends(get_current_user),
    note_service: NoteService = Depends(get_note_service),
):
    return note_service.get_author_note(author_id=current_user.id, note_id=note_id)


@router.delete(
    "/delete/{note_id}",
    description="Удалить заметку",
    response_model=Status,
)
def delete_note(
    note_id: int,
    current_user: UserOutSchema = Depends(get_current_user),
    note_service: NoteService = Depends(get_note_service),
) -> Status:
    return note_service.delete_note(author_id=current_user.id, note_id=note_id)
