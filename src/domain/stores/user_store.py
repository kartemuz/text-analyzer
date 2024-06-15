from ..models import User
from abc import abstractmethod, ABC
from typing import List, Optional


class UserStore(ABC):
    @abstractmethod
    async def get(self, login: str, password: str) -> User:
        pass

    @abstractmethod
    async def edit(self, user: User) -> bool:
        pass

    @abstractmethod
    async def add(self, user: User) -> None:
        pass

    @abstractmethod
    async def delete(self, login: Optional[str], password: Optional[str], user: Optional[User]) -> bool:
        pass

    @abstractmethod
    async def get_all_logins(self) -> List[str]:
        pass
