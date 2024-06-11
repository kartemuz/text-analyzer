from .. domain.stores import UserStore


class NewsSourceService:
    def __init__(self, store: UserStore):
        self.store: UserStore = store
