from typing import Annotated
from fastapi import Depends

from app.dependencies.clients.db_session import SessionMakerDep
from app.uow.user import IUserUoW, UserUoW


def create_user_uow(session_maker: SessionMakerDep):
    return UserUoW(session_maker)


UserUoWDep = Annotated[IUserUoW, Depends(create_user_uow)]
