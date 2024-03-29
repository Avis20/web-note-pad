import logging
from uuid import UUID
from passlib.context import CryptContext

from app.dto.users import UserCreateDTO, UserDTO
from app.exceptions.users import UserException
from app.schemas.request.users import UserLoginSchema, UserRegistrationSchema
from app.uow.users import IUserUoW


logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, user_uow: IUserUoW):
        self.user_uow = user_uow
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def _verify_password(self, plan_password: str, hashed_password: str) -> bool:
        """Валидация пароля."""
        return self.pwd_context.verify(plan_password, hashed_password)

    async def delete_user(self, user_id: UUID) -> UserDTO:
        """
        Удаление данных о пользователе

        Raises:
            UserException.UserNotFoundException
        """
        async with self.user_uow:
            user_dto = await self.user_uow.user_repo.delete_user_by_id(user_id=user_id)
            if not user_dto:
                raise UserException.UserNotFoundException(f"User with '{user_id}' not found")
            logger.debug(f"User '{user_dto}' was deleted!")
            return user_dto

    async def get_user_by_id(self, user_id: UUID) -> UserDTO:
        """
        Получение данных о пользователе
        Raises:
            UserException.UserNotFoundException
        """
        async with self.user_uow:
            user_dto = await self.user_uow.user_repo.get_user_by_id(user_id=user_id)
            if not user_dto:
                raise UserException.UserNotFoundException(f"User with '{user_id}' not found")
            logger.debug(f"Get user by id '{user_id}'='{user_dto}'")
            return user_dto

    async def user_login(self, login_data: UserLoginSchema) -> UserDTO:
        """
        Авторизация пользователя в системе

        Raises:
            UserException.UserNotFoundException
        """
        user_dto = None
        async with self.user_uow:
            user_dto = await self.user_uow.user_repo.get_user_by_username(login_data.username)
            if not user_dto:
                raise UserException.UserNotFoundException(f'User with {login_data.username} not found')

            logger.debug(f"Get user by user name '{login_data.username}'='{user_dto.safe_data()}'")
            if not self._verify_password(login_data.password, user_dto.password):
                raise UserException.UserForbiddenException("Wrong password")

            return user_dto

    async def create_user(self, user_data: UserRegistrationSchema) -> UserDTO | None:
        """
        Создание пользователя

        Raises:
            UserException.UserAlreadyExists
        """
        encrypt_user_password = self.pwd_context.encrypt(user_data.password)
        user_create_dto = UserCreateDTO(
            username=user_data.username,
            password=encrypt_user_password,
            full_name=user_data.full_name,
        )
        async with self.user_uow:
            user_dto = await self.user_uow.user_repo.create_user(user_create_dto)
            return user_dto
