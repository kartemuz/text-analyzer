from typing import List, Optional

from src.domain.stores import NewsSourceStore
from src.domain.models import NewsSource
from sqlalchemy import select
from ..database.models import NewsSourceDB
from ..database.base import session_factory


class NewsSourceRepository(NewsSourceStore):
    async def get_news_source_db_(self, name) -> Optional[NewsSourceDB]:
        result: Optional[NewsSourceDB]
        async with session_factory() as session:
            query = select(NewsSourceDB).where(NewsSourceDB.name == name)
            query_result = await session.execute(query)
            result = query_result.scalar()
        return result

    async def get_by_name(self, name: str) -> Optional[NewsSource]:
        result: Optional[NewsSource]
        async with session_factory() as session:
            query = select(NewsSourceDB).where(NewsSourceDB.name == name)
            query_result = await session.execute(query)
            result = query_result.scalar()
        return result

    async def edit(self, news_source: NewsSource) -> bool:
        result: bool
        news_source_db = await self.get_news_source_db_(news_source.name)
        if news_source_db is not None:
            async with session_factory() as session:
                await session.delete(news_source_db)
                await self.add(news_source)
                result = True
        else:
            result = False
        return result

    async def add(self, news_source: NewsSource) -> None:
        async with session_factory() as session:
            news_source_db = NewsSourceDB(
                name=news_source.name,
                rss_url=news_source.rss_url
            )
            session.add(news_source_db)
            await session.commit()

    async def delete(self, name: str) -> bool:
        result: bool
        news_source_db = await self.get_news_source_db_(name)
        if news_source_db is not None:
            async with session_factory() as session:
                await session.delete(news_source_db)
                await session.commit()
                result = True
        else:
            result = False
        return result

    async def get_all(self) -> List[NewsSource]:
        result: Optional[List[NewsSource]]
        async with session_factory() as session:
            query = select(NewsSourceDB)
            query_result = await session.execute(query)
            result = query_result.scalars()
        return result
