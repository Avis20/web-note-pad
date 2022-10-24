# ./backend/src/settings.py

from pydantic import BaseSettings
from functools import lru_cache


class Config(BaseSettings):

    PG_MASTER_USER: str = "web_notepad"
    PG_MASTER_PASSWORD: str = "1234"
    PG_MASTER_DB_NAME: str = "web_notepad"

    PG_MASTER_HOST: str = "localhost"
    PG_MASTER_PORT: int = 5432

    DB_ECHO_LOG: bool = True
    APP_NAME: str = "web_notepad"

    @property
    def db_master_uri(self) -> str:
        return (
            f"postgresql+psycopg2://{self.PG_MASTER_USER}:{self.PG_MASTER_PASSWORD}@"
            f"{self.PG_MASTER_HOST}:{self.PG_MASTER_PORT}/{self.PG_MASTER_DB_NAME}?"
            f"application_name={self.APP_NAME}"
        )

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Config:
    return Config()
