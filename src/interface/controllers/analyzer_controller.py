from src.application.services import AnalyzerService
from typing import Dict, List
from src.domain.models import User


class AnalyzerController:
    analyzer_service: AnalyzerService

    def __init__(self):
        self.analyzer_service = AnalyzerService()

    async def search(self, user: User) -> Dict[str, List[str]]:
        result = await self.analyzer_service.search(user)
        return result
