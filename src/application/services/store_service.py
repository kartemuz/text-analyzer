from src.domain.stores import Store


class StoreService:
    store: Store

    def __init__(self, store: Store):
        self.store: Store = store()

    async def create_store(self):
        await self.store.create_store()
