from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy import insert, select, delete
from sqlalchemy.exc import IntegrityError

from app.dto.users import UserCreateDTO, UserDTO
from app.exceptions.users import UserException
from app.repositories.base import SQLAlchemyRepository
from app.models.users import User


class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user_data: UserCreateDTO) -> UserDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_username(self, username: str) -> UserDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_id(self, user_id: UUID) -> UserDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def delete_user_by_id(self, user_id: UUID) -> UserDTO | None:
        raise NotImplementedError


class UserRepository(IUserRepository, SQLAlchemyRepository):
    async def delete_user_by_id(self, user_id: UUID) -> UserDTO | None:
        user_dto = await self.get_user_by_id(user_id)
        if not user_dto:
            return None

        stmt_delete = delete(User).filter_by(id=user_dto.id)
        await self._session.execute(stmt_delete)
        return user_dto

    async def get_user_by_id(self, user_id: UUID) -> UserDTO | None:
        stmt = select(User).filter_by(id=user_id)
        result = await self._session.execute(stmt)
        if user := result.scalar():
            return UserDTO.model_to_dto(user)
        return None

    async def get_user_by_username(self, username: str) -> UserDTO | None:
        stmt = select(User).filter_by(username=username)
        result = await self._session.execute(stmt)
        if user := result.scalar():
            return UserDTO.model_to_dto(user)
        return None

    async def create_user(self, user_data: UserCreateDTO) -> UserDTO | None:
        stmt = insert(User).values(user_data.as_dict()).returning(User)
        try:
            result = await self._session.execute(stmt)
            if user := result.scalar():
                return UserDTO.model_to_dto(user)
        except IntegrityError:
            raise UserException.UserExistsException(
                f"User with username '{user_data.username}' already exists in database",
            )
        return None
