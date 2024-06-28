from src.interface.controllers import UserController
from src.domain.models import User
from src.domain import exceptions
from typing import List


class UserSessionController:
    user_controller: UserController
    user: User

    def __init__(self, login: str, password: str) -> None:
        self.user_controller = UserController()
        self.user = User(login=login, password=password)

    # Фабричный метод создания объекта
    async def create(self, is_new: bool):
        # Создание нового пользователя
        if is_new:
            try:
                await self.user_controller.add(self.user)
                self.user = await self.user_controller.get(login=self.user.login, password=self.user.password)
            except exceptions.LoginNotUniqueException as ex:
                raise ex

        # Авторизация существующего пользователя
        else:
            try:
                self.user = await self.user_controller.get(login=self.user.login, password=self.user.password)
            except exceptions.InvalidLoginException as ex:
                raise ex
            except exceptions.InvalidPasswordException as ex:
                raise ex

        return self

    async def edit(self, user) -> bool:
        result: bool
        self.user = user
        result = await self.user_controller.edit(self.user)
        return result

    async def add_tags(self, tags: List[str]) -> bool:
        result: bool
        self.user.add_tags(tags)
        result = await self.edit(self.user)
        return result

    async def add_tag(self, tag: str) -> bool:
        result: bool
        self.user.add_tag(tag)
        result = await self.edit(self.user)
        return result

    async def delete(self) -> bool:
        result = await self.user_controller.delete(login=self.user.login, password=self.user.password)
        return result
