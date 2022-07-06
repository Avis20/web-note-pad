# ./backend/models/database.py

from databases import Database
from src.settings import get_settings

settings = get_settings()

database = Database(settings.DATABASE_URL)
