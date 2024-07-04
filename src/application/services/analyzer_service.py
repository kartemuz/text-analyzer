from src.application.analyzer import Analyzer
from src.domain.models import User
from src.application.services import NewsSourceService
from src.persistence.repositories import NewsSourceRepository
from src.domain.schemas.rss import Item
from typing import Dict, List
from src.domain.schemas.responses import AnalyzerResponse
from datetime import datetime


class AnalyzerService:
    analyzer: Analyzer

    def __init__(self):
        self.analyzer = Analyzer()

    async def search(self, user: User) -> Dict[str, List[AnalyzerResponse]]:
        result: Dict[str, List[AnalyzerResponse]] = dict()

        for t in user.tags:
            result[t] = []
            for i in await self.search_by_tag(t):
                result[t].append(i)

        return result

    async def search_by_tag(self, tag: str) -> List[AnalyzerResponse]:
        result = []
        news_source_service = NewsSourceService(store=NewsSourceRepository)
        news_sources = await news_source_service.get_all()
        for ns in news_sources:
            for i in ns.rss.channel.content.items:
                i: Item
                if self.analyzer.search(i.description.content, tag) or self.analyzer.search(i.title.content, tag) or \
                        (i.category is not None and self.analyzer.search(i.category.content, tag)):
                    date_obj = datetime.strptime(i.pub_date.content, "%a, %d %b %Y %H:%M:%S %z")

                    # Преобразование объекта datetime в строку в формате дд.мм.гггг
                    formatted_date = date_obj.strftime("%d.%m.%Y")
                    analyzer_response = AnalyzerResponse(
                        source_name=ns.name,
                        title=i.title.content,
                        link=i.link.content,
                        date=formatted_date
                    )
                    result.append(analyzer_response)
        return result
