# Конфигурационный файл


from typing import Final
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: Final = True
    TEST: Final = True
    DB_NAME: str

    @property
    def db_url(self):
        result: str
        if self.TEST:
            result = f"sqlite+aiosqlite:///../../static/{self.DB_NAME}"
        else:
            result = f"sqlite+aiosqlite:///../static/{self.DB_NAME}"
        return result

    model_config = SettingsConfigDict(
        env_file="../../.env" if TEST else "../.env"
    )


settings = Settings()
