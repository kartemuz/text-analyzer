from src.domain.stores import NewsSourceStore


class NewsSourceService:
    store: NewsSourceStore

    def __init__(self, store: NewsSourceStore):
        self.store: NewsSourceStore = store
