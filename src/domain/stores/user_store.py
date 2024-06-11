from ..models import User
from abc import abstractmethod, ABC


class UserStore(ABC):
    @abstractmethod
    async def get_by_name(self, name: str) -> User:
        pass

    @abstractmethod
    async def edit(self, obj: User):
        pass

    @abstractmethod
    async def add(self, obj: User):
        pass

    @abstractmethod
    async def delete_by_name(self, name: str):
        pass
