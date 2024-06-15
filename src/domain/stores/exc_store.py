class StoreException(Exception):
    def __init__(self, message, extra_info):
        super().__init__(message)
        self.extra_info = extra_info


class LoginNotUniqueException(StoreException):
    pass


class NewsSourceNotUnique(StoreException):
    pass
