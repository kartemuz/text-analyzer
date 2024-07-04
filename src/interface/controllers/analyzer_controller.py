from src.application.services import AnalyzerService
from typing import Dict, List
from src.domain.models import User
from src.domain.schemas.responses import AnalyzerResponse


class AnalyzerController:
    analyzer_service: AnalyzerService

    def __init__(self):
        self.analyzer_service = AnalyzerService()

    async def search(self, user: User) -> Dict[str, List[AnalyzerResponse]]:
        result = await self.analyzer_service.search(user)
        return result

    async def search_by_tag(self, tag: str) -> List[AnalyzerResponse]:
        result = await self.analyzer_service.search_by_tag(tag)
        return result
