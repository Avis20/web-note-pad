from app.uow.user import IUserUoW


class UserService:
    def __init__(self, user_uow: IUserUoW):
        self.user_uow = user_uow

    async def create_user(self):
        async with self.user_uow:
            await self.user_uow.user_repo.create_user()
