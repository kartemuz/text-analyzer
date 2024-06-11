from ..domain.stores import NewsSourceStore
from ..domain.models import NewsSource


class NewsSourceRepository(NewsSourceStore):
    model = None

    async def get_by_name(self, name: str) -> NewsSource:
        pass

    async def edit(self, obj: NewsSource):
        pass

    async def add(self, obj: NewsSource):
        pass

    async def delete_by_name(self, name: str):
        pass
