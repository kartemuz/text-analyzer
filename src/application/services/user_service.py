from src.domain.stores import UserStore
from src.domain.models import User
from typing import Optional, List
from src.application.customizer.default_data import default_data


class UserService:
    store: UserStore

    def __init__(self, store: UserStore):
        self.store: UserStore = store()

    async def add(self, user: User) -> None:
        await self.store.add(user)

    async def get(self, login: str, password: str) -> Optional[User]:
        result = await self.store.get(login=login, password=password)
        return result

    async def edit(self, user: User) -> bool:
        result = await self.store.edit(user)
        return result

    async def delete(self, login: str, password: str) -> bool:
        result = await self.store.delete(login=login, password=password, user=None)
        return result

    async def get_all_logins(self) -> List[str]:
        result = await self.store.get_all_logins()
        return result

    async def create_default(self) -> None:
        for u in default_data.users:
            user = User(login=u.login, password=u.password, tags=u.tags)
            await self.add(user)
