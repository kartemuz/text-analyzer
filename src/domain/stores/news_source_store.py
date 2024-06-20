from ..models import NewsSource
from abc import abstractmethod, ABC
from typing import List, Optional


class NewsSourceStore(ABC):
    @abstractmethod
    async def get(self, name: str) -> Optional[NewsSource]:
        pass

    @abstractmethod
    async def edit(self, news_source: NewsSource) -> bool:
        pass

    @abstractmethod
    async def add(self, news_source: NewsSource) -> None:
        pass

    @abstractmethod
    async def delete(self, name: Optional[str], news_source: Optional[NewsSource]) -> bool:
        pass

    @abstractmethod
    async def get_all(self) -> List[NewsSource]:
        pass
