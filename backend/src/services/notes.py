# ./backend/src/services/notes.py

from sqlalchemy.sql import select

from src.models.database import database
from src.models.notes import Notes

async def get_note_list(author_id: int):
    query = select(Notes).filter_by(author_id=author_id)

    rows = await database.fetch_all(query)
    print('\n\n')
    print(rows)
    print('\n\n')
