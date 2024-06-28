from src.application.analyzer import Analyzer
from src.domain.models import User
from src.application.services import NewsSourceService
from src.persistence.repositories import NewsSourceRepository
from src.domain.schemas.rss import Item
from typing import Dict, List
from src.domain.schemas.responses import AnalyzerResponse


class AnalyzerService:
    analyzer: Analyzer

    def __init__(self):
        self.analyzer = Analyzer()

    async def search(self, user: User) -> Dict[str, List[AnalyzerResponse]]:
        result: Dict[str, List[AnalyzerResponse]] = dict()

        news_source_service = NewsSourceService(store=NewsSourceRepository)
        news_sources = await news_source_service.get_all()

        for t in user.tags:
            result[t] = []
            for ns in news_sources:
                for i in ns.rss.channel.content.items:
                    i: Item
                    if self.analyzer.search(i.description.content, t) or self.analyzer.search(i.title.content, t) or \
                            (i.category is not None and self.analyzer.search(i.category.content, t)):
                        analyzer_response = AnalyzerResponse(
                            source_name=ns.name,
                            title=i.title.content,
                            link=i.link.content,
                            date=i.pub_date.content
                        )
                        result[t].append(analyzer_response)

        return result
