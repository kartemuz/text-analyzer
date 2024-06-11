from .. domain.stores import NewsSourceStore


class NewsSourceService:
    def __init__(self, store: NewsSourceStore):
        self.store: NewsSourceStore = store
