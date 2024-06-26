from src.application.services import NewsSourceService
from src.persistence.repositories import NewsSourceRepository
from src.domain.models import NewsSource
from typing import Optional, List


class NewsSourceController:
    news_source_service: NewsSourceService

    def __init__(self):
        self.news_source_service = NewsSourceService(store=NewsSourceRepository)

    async def get(self, name: str) -> Optional[NewsSource]:
        result = await self.news_source_service.get(name=name)
        return result

    async def edit(self, news_source: NewsSource) -> bool:
        result = await self.news_source_service.edit(news_source=news_source)
        return result

    async def add(self, news_source: NewsSource) -> None:
        await self.news_source_service.add(news_source=news_source)

    async def delete(self, name: str) -> bool:
        result = await self.news_source_service.delete(name=name)
        return result

    async def get_all(self) -> List[NewsSource]:
        result = await self.news_source_service.get_all()
        return result

    async def create_default(self) -> None:
        await self.news_source_service.create_default()
