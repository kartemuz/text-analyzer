from typing import List, Optional

from src.domain.stores import NewsSourceStore, exc_store
from src.domain.models import NewsSource
from sqlalchemy import select, exc
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

    async def get(self, name: str) -> Optional[NewsSource]:
        result: Optional[NewsSource]
        news_source_db = await self.get_news_source_db_(name)
        result = NewsSource(name=news_source_db.name, rss_url=news_source_db.rss_url)
        return result

    async def edit(self, news_source: NewsSource) -> bool:
        result: bool
        news_source_db = await self.get_news_source_db_(news_source.name)
        if news_source_db is not None:
            await self.delete(name=news_source.name)
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
            try:
                await session.commit()
            except exc.IntegrityError:
                await session.rollback()
                raise exc_store.NewsSourceNotUnique(message='A similar news source already exists',
                                                    extra_info={'name': news_source.name,
                                                                'rss_url': news_source.rss_url})

    async def delete(self, name: Optional[str], news_source: Optional[NewsSource]) -> bool:
        result: bool
        news_source_db: NewsSourceDB
        if news_source is None:
            news_source_db = await self.get_news_source_db_(name)
        else:
            news_source_db = await self.get_news_source_db_(news_source.name)
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
            result = [NewsSource(name=i.name, rss_url=i.rss_url) for i in query_result.scalars()]
        return result
