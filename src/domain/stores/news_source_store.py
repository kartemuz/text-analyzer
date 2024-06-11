from ..models import NewsSource
from abc import abstractmethod, ABC


class NewsSourceStore(ABC):
    @abstractmethod
    async def get_by_name(self, name: str) -> NewsSource:
        pass

    @abstractmethod
    async def edit(self, obj: NewsSource):
        pass

    @abstractmethod
    async def add(self, obj: NewsSource):
        pass

    @abstractmethod
    async def delete_by_name(self, name: str):
        pass
