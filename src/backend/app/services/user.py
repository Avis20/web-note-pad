from passlib.context import CryptContext

from app.dto.user import UserCreateDTO, UserDTO
from app.exceptions.user import UserException
from app.schemas.request.user import UserLoginSchema, UserRegistrationSchema
from app.uow.user import IUserUoW


class UserService:
    def __init__(self, user_uow: IUserUoW):
        self.user_uow = user_uow
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def _verify_password(self, plan_password: str, hashed_password: str) -> bool:
        """Валидация пароля."""
        return self.pwd_context.verify(plan_password, hashed_password)

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
