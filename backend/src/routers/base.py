# ./backend/src/routers/base.py

from fastapi import APIRouter

"""
Базовый роут для хранения всех роутов
"""

from src.routers import root
from src.routers.v1 import users, notes

api_router = APIRouter()
api_router.include_router(root.router, tags=["root"])
api_router.include_router(users.router, tags=["Users"], prefix="/v1/user")
api_router.include_router(notes.router, tags=["Notes"], prefix="/v1/note")
