class BaseExc(Exception):
    def __init__(self, message, extra_info):
        super().__init__(message)
        self.extra_info = extra_info


class LoginNotUniqueException(BaseExc):
    """Логин уже используется (некорректный логин при создании нового пользователя)"""


class NewsSourceNotUniqueException(BaseExc):
    """Новостной источник с таким rss_url или name уже существует"""


class InvalidPasswordException(BaseExc):
    """Некорректный пароль при авторизации"""


class InvalidLoginException(BaseExc):
    """Некорректный логин при авторизации"""
