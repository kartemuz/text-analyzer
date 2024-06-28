from src.application.services import UserService
from src.persistence.repositories import UserRepository
from src.domain.models import User
from typing import Optional, List
from src.domain import exceptions


class UserController:
    user_service: UserService

    def __init__(self):
        self.user_service = UserService(store=UserRepository)

    async def add(self, user: User) -> None:
        try:
            await self.user_service.add(user)
        except exceptions.LoginNotUniqueException as ex:
            raise ex

    async def get(self, login: str, password: str) -> Optional[User]:
        result = await self.user_service.get(login=login, password=password)
        if result is None:
            all_logins = await self.get_all_logins()
            if login in all_logins:
                raise exceptions.InvalidPasswordException
            else:
                raise exceptions.InvalidLoginException
        return result

    async def edit(self, user: User) -> bool:
        result = await self.user_service.edit(user)
        return result

    async def delete(self, login: str, password: str) -> bool:
        result = await self.user_service.delete(login=login, password=password)
        return result

    async def get_all_logins(self) -> List[str]:
        result = await self.user_service.get_all_logins()
        return result

    async def create_default(self) -> None:
        await self.user_service.create_default()
