from abc import ABC, abstractmethod

from app.models.users import User
from app.repositories.base import SQLAlchemyRepository
from sqlalchemy import select


class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self):
        raise NotImplementedError


class UserRepository(IUserRepository, SQLAlchemyRepository):
    async def create_user(self):
        stmt = select(User)
        result = await self._session.execute(stmt)
        if user := result.scalar:
            user
            ...
