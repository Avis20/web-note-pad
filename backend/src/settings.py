# ./backend/src/settings.py

from pydantic import BaseSettings
from functools import lru_cache


class Config(BaseSettings):
    DATABASE_URL: str = ""
    DB_ECHO_LOG: bool = True


@lru_cache
def get_settings() -> Config:
    return Config()
