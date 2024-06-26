# Конфигурационный файл


from typing import Final
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: Final = True
    TEST: Final = True
    DB_NAME: str
    STATIC_DIR: Final = 'static'

    LOG_DIR: Final = 'logs'
    LOG_FORMAT: Final = '{time} {level} {message}'
    LOG_ROTATION: Final = '00:00'
    LOG_FILE_NAME: Final = '{time}.log'

    @property
    def db_url(self) -> str:
        result: str
        db_name: Final = 'sqlite'
        db_engine: Final = 'aiosqlite'
        if self.TEST:
            result = f"{db_name}+{db_engine}:///../../{self.STATIC_DIR}/{self.DB_NAME}"
        else:
            result = f"{db_name}+{db_engine}:///../{self.STATIC_DIR}/{self.DB_NAME}"
        return result

    @property
    def data_path(self) -> str:
        result: str
        data_file_name: Final = "data.json"
        if self.TEST:
            result = f"../../{self.STATIC_DIR}/{data_file_name}"
        else:
            result = f"../{self.STATIC_DIR}/{data_file_name}"
        return result

    model_config = SettingsConfigDict(
        env_file="../../.env" if TEST else "../.env"
    )


settings = Settings()
