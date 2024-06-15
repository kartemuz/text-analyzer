from src.domain.stores import Store
from src.persistence.database import base, models


class StoreRepository(Store):
    async def create_store(self) -> None:
        async with base.engine.begin() as conn:
            await conn.run_sync(base.BaseDB.metadata.drop_all)
            await conn.run_sync(base.BaseDB.metadata.create_all)
