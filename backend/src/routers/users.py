
from fastapi import APIRouter
from src.schemas.users import UserOutSchema

router = APIRouter()


@router.post('/register', response_model=UserOutSchema)
async def create_user():
    pass
