# ./backend/src/routers/root.py

from fastapi import APIRouter

"""
Root роут
"""

router = APIRouter()


@router.get("/")
def root():
    return "Hello WebNotepad"
