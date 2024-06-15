from ..models import NewsSource
from abc import abstractmethod, ABC
from typing import List


class NewsSourceStore(ABC):
    @abstractmethod
    async def get_by_name(self, name: str) -> NewsSource:
        pass

    @abstractmethod
    async def edit(self, news_source: NewsSource) -> bool:
        pass

    @abstractmethod
    async def add(self, news_source: NewsSource) -> None:
        pass

    @abstractmethod
    async def delete(self, name: str) -> bool:
        pass

    @abstractmethod
    async def get_all(self) -> List[NewsSource]:
        pass
