from src.application.analyzer import Analyzer
from src.domain.models import User
from src.application.services import NewsSourceService
from src.persistence.repositories import NewsSourceRepository
from src.domain.schemas.rss import Item
from typing import Dict, List


class AnalyzerService:
    analyzer: Analyzer

    def __init__(self):
        self.analyzer = Analyzer()

    async def search(self, user: User) -> Dict[str, List[str]]:
        result: Dict[str, List[str]] = dict()

        news_source_service = NewsSourceService(store=NewsSourceRepository)
        news_sources = await news_source_service.get_all()

        for t in user.tags:
            result[t] = []
            for ns in news_sources:
                for i in ns.rss.channel.content.items:
                    i: Item
                    if self.analyzer.search(i.description.content, t) \
                            or self.analyzer.search(i.title.content, t):
                        result[t].append(i.link.content)
                    if i.category is not None and self.analyzer.search(i.category.content, t):
                        result[t].append(i.link.content)

        return result
