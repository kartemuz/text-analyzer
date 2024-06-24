from src.domain.stores import NewsSourceStore
from src.domain.models import NewsSource
from typing import Optional, List
from src.application.customizer.default_data import default_data


class NewsSourceService:
    store: NewsSourceStore

    def __init__(self, store: NewsSourceStore):
        self.store: NewsSourceStore = store()

    async def get(self, name: str) -> Optional[NewsSource]:
        result = await self.store.get(name=name)
        return result

    async def edit(self, name: str, rss_url: str) -> bool:
        news_source = await NewsSource(name=name, rss_url=rss_url).create()
        result = await self.store.edit(news_source=news_source)
        return result

    async def add(self, name: str, rss_url: str) -> None:
        news_source = await NewsSource(name=name, rss_url=rss_url).create()
        await self.store.add(news_source=news_source)

    async def delete(self, name: str) -> bool:
        result = await self.store.delete(name=name, news_source=None)
        return result

    async def get_all(self) -> List[NewsSource]:
        result = await self.store.get_all()
        return result

    async def create_default(self) -> None:
        for s in default_data.news_sources:
            await self.add(name=s.name, rss_url=s.rss_url)
