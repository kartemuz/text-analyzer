from src.persistence.database import base, models
from src.application.services import StoreService
from src.persistence.repositories import StoreRepository


class StoreController:
    @staticmethod
    async def create_store():
        store_service = StoreService(store=StoreRepository)
        await store_service.create_store()
