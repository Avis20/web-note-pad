from __future__ import annotations

from app.repositories.user import IUserRepository, UserRepository
from app.uow.base import SQLAlchemyUoW, UnitOfWorkABC


class IUserUoW(UnitOfWorkABC):
    user_repo: IUserRepository


class UserUoW(SQLAlchemyUoW, IUserUoW):
    async def __aenter__(self) -> UserUoW:
        await super().__aenter__()
        self.user_repo = UserRepository(self.session)
        return self
