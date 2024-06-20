from src.domain.stores import NewsSourceStore
from src.domain.models import NewsSource
from typing import Optional, List


class NewsSourceService:
    store: NewsSourceStore

    def __init__(self, store: NewsSourceStore):
        self.store: NewsSourceStore = store()

    async def get(self, name: str) -> Optional[NewsSource]:
        result = await self.store.get(name=name)
        return result

    async def edit(self, name: str, rss_url: str) -> bool:
        news_source = NewsSource(name=name, rss_url=rss_url)
        result = await self.store.edit(news_source)
        return result

    async def add(self, name: str, rss_url: str) -> None:
        news_source = NewsSource(name=name, rss_url=rss_url)
        await self.store.add(news_source)

    async def delete(self, name: str) -> bool:
        result = await self.store.delete(name)
        return result

    async def get_all(self) -> List[NewsSource]:
        result = await self.store.get_all()
        return result
