from ..domain.stores import UserStore
from ..domain.models import User


class UserRepository(UserStore):
    model = None

    async def get_by_login(self, name: str) -> User:
        pass

    async def edit(self, obj: User):
        pass

    async def add(self, obj: User):
        pass

    async def delete_by_login(self, name: str):
        pass
