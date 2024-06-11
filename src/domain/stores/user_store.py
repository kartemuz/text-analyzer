from ..models import User
from abc import abstractmethod, ABC


class UserStore(ABC):
    @abstractmethod
    async def get_by_login(self, login: str) -> User:
        pass

    @abstractmethod
    async def edit(self, obj: User):
        pass

    @abstractmethod
    async def add(self, obj: User):
        pass

    @abstractmethod
    async def delete_by_login(self, login: str):
        pass
