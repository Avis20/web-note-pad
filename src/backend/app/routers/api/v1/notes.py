from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, status
import logging

from app.dependencies import NoteServiceDep
from app.dependencies.auth import get_current_user
from app.dto.users import UserDTO
from app.schemas.request.notes import NoteCreateSchema, NoteListSchema, NoteUpdateSchema
from app.schemas.response.base import ResponseSchema
from app.schemas.response.notes import NoteListResponseSchema, NoteResponseSchema


router = APIRouter(prefix="/note")

logger = logging.getLogger()


@router.post(
    '/add',
    summary="Добавление заметки",
    description="Создание новой заметки",
    status_code=status.HTTP_201_CREATED,
    response_model=NoteResponseSchema,
)
async def _add_note(
    request_note: NoteCreateSchema,
    user_dto: Annotated[UserDTO, Depends(get_current_user)],
    note_service: NoteServiceDep,
):
    note_dto = await note_service.create_note(request_note, user_dto)
    return {"success": 1, "item": note_dto, "params": request_note.model_dump()}


@router.get(
    '/{note_id}/get',
    summary="Получение заметки",
    description="Получение созданной заметки",
    response_model=NoteResponseSchema,
)
async def _get_note(
    note_id: UUID,
    user_dto: Annotated[UserDTO, Depends(get_current_user)],
    note_service: NoteServiceDep,
):
    note_dto = await note_service.get_note(note_id, user_dto)
    return {"success": 1, "item": note_dto, "params": {"note_id": note_id}}


@router.post(
    '/{note_id}/update',
    summary="Изменение заметки",
    description="Изменение заметки",
    response_model=NoteResponseSchema,
)
async def _note_update(
    note_id: UUID,
    request_note: NoteUpdateSchema,
    user_dto: Annotated[UserDTO, Depends(get_current_user)],
    note_service: NoteServiceDep,
):
    note_dto = await note_service.note_update(request_note, note_id, user_dto)
    return {"success": 1, "item": note_dto, "params": {"note_id": note_id, **request_note.model_dump()}}


@router.delete(
    '/{note_id}/delete',
    summary="Удаление заметки",
    description="Удаление созданной заметки",
    response_model=ResponseSchema,
)
async def _delete_note(
    note_id: UUID,
    user_dto: Annotated[UserDTO, Depends(get_current_user)],
    note_service: NoteServiceDep,
):
    await note_service.delete_note(note_id, user_dto)
    return {"success": 1}


@router.post(
    '/list',
    summary="Список заметок",
    description="Получение списка заметок",
    response_model=NoteListResponseSchema,
)
async def _note_list(
    note_request: NoteListSchema,
    user_dto: Annotated[UserDTO, Depends(get_current_user)],
    note_service: NoteServiceDep,
):
    notes = await note_service.get_note_list(note_request, user_dto)
    return {"success": 1, "list": notes, "params": note_request.model_dump()}
