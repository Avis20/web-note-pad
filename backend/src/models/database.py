# ./backend/models/database.py

from databases import Database
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from src.settings import get_settings

settings = get_settings()

metadata = MetaData()
BaseModel = declarative_base(metadata=metadata)

database = Database(settings.DATABASE_URL)
