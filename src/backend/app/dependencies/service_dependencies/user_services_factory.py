from typing import Annotated

from app.dependencies import UserUoWDep
from app.services.user import UserService
from fastapi import Depends


def create_user_service(user_uow: UserUoWDep):
    return UserService(user_uow)


UserServiceDep = Annotated[UserService, Depends(create_user_service)]
