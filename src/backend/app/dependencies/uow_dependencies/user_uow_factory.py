from typing import Annotated

from app.dependencies.clients.db_session import SessionMakerDep
from app.uow.user import IUserUoW, UserUoW
from fastapi import Depends


def create_user_uow(
    session_maker: SessionMakerDep,
):
    return UserUoW(session_maker)


UserUoWDep = Annotated[IUserUoW, Depends(create_user_uow)]
