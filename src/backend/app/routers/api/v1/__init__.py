from fastapi import APIRouter

from .users import router as user_router
from .notes import router as note_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(user_router)
v1_router.include_router(note_router)
