from src.domain.stores import UserStore


class UserService:
    store: UserStore

    def __init__(self, store: UserStore):
        self.store: UserStore = store
