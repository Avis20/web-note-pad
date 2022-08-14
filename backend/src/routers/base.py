from fastapi import APIRouter

from src.routers import root, users, notes

api_router = APIRouter()
api_router.include_router(root.router, tags=["root"])
api_router.include_router(users.router, tags=["Users"], prefix="/user")
api_router.include_router(notes.router, tags=["Notes"], prefix="/note")

