from src.interface.controllers import UserController, AnalyzerController
from src.domain.models import User
from src.domain import exceptions
from typing import List, Dict
from src.domain.schemas.responses import AnalyzerResponse


class UserSessionController:
    user_controller: UserController
    analyzer_controller: AnalyzerController
    user: User

    def __init__(self, login: str, password: str) -> None:
        self.user_controller = UserController()
        self.analyzer_controller = AnalyzerController()
        self.user = User(login=login, password=password)

    # Фабричный метод создания объекта
    async def create(self, is_new: bool = False):
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

    async def add_tag(self, tag: str) -> bool:
        result: bool
        self.user.add_tag(tag)
        result = await self.user_controller.edit(self.user)
        return result

    async def delete_tag(self, tag: str) -> bool:
        result: bool
        self.user.delete_tag(tag)
        result = await self.user_controller.edit(self.user)
        return result

    async def delete(self) -> bool:
        result = await self.user_controller.delete(login=self.user.login, password=self.user.password)
        return result

    async def change_password(self, new_password: str) -> None:
        await self.user_controller.delete(self.user.login, self.user.password)
        self.user = User(login=self.user.login, password=new_password, tags=self.user.tags)
        await self.user_controller.add(self.user)

    def get_tags(self) -> List[str]:
        result = self.user.get_tags()
        return result

    async def search(self) -> Dict[str, List[AnalyzerResponse]]:
        result = await self.analyzer_controller.search(self.user)
        return result
