# ./backend/src/routers/notes.py


from fastapi import APIRouter, Depends

import src.services.notes as note_services
from src.internal.auth.jwthandler import get_current_user
from src.schemas.users import UserOutSchema


router = APIRouter()

@router.get(
    '/note/list',
    description="Получение списка заметок пользователя"
)
async def note_list(current_user: UserOutSchema = Depends(get_current_user)):
    return await note_services.get_note_list(author_id=current_user.id)
