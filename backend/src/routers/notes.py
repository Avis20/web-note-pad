# ./backend/src/routers/notes.py


from fastapi import APIRouter, Depends

import src.services.notes as note_services
from src.internal.auth.jwthandler import get_current_user

router = APIRouter()

@router.get(
    '/note/list',
    description="Получение списка заметок пользователя",
    dependencies=[Depends(get_current_user)]
)
async def note_list():
    await note_services.get_note_list()