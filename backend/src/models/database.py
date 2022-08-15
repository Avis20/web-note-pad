# ./backend/models/database.py
"""
Модуль для работы с БД
"""
import logging
import sys
from databases import Database
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from src.settings import get_settings

settings = get_settings()

if settings.DB_ECHO_LOG:
    logger = logging.StreamHandler(sys.stdout)

    logger_db = logging.getLogger("databases")
    logger_db.setLevel(logging.DEBUG)
    logger_db.addHandler(logger)

metadata = MetaData()
BaseModel = declarative_base(metadata=metadata)

database = Database(settings.DATABASE_URL)
