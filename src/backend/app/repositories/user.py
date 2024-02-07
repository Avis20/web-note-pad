from abc import ABC, abstractmethod
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from app.dto.user import UserCreateDTO, UserDTO
from app.exceptions.user import UserException
from app.repositories.base import SQLAlchemyRepository
from app.models.users import User


class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user_data: UserCreateDTO) -> UserDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_username(self, username: str) -> UserDTO | None:
        raise NotImplementedError


class UserRepository(IUserRepository, SQLAlchemyRepository):
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
