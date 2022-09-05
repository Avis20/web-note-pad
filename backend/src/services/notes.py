# ./backend/src/services/notes.py

from fastapi import status, HTTPException
from sqlalchemy.sql import select, insert, delete
from psycopg2.errors import UniqueViolation

from src.models.database import database
from src.models.notes import Notes
from src.models.users import Users
from src.schemas.notes import NoteInSchema, NotesOutSchema
from src.schemas.base import Status


async def get_note_list(author_id: int):
    query = select(Notes).filter_by(author_id=author_id).order_by(Notes.id.desc())
    rows = await database.fetch_all(query)
    # TODO: add author
    return rows


async def get_note(note_id: int):
    note_obj = None
    query = select(Notes, Users).join(Users).where(Notes.id == note_id)

    # for row in await database.fetch_all(query):
    #    print(f"{row.Notes.name} {row.Address.email_address}")

    try:
        note_obj = await database.fetch_one(query)
    except Exception as e:
        print(e)

    if note_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

    return NotesOutSchema.from_orm(note_obj)


async def add_note(author_id: int, note: NoteInSchema) -> NotesOutSchema:
    note_dict = note.dict(exclude_none=True)
    note_dict["author_id"] = author_id
    query = insert(Notes).values(note_dict).returning(Notes)

    try:
        note_obj = await database.fetch_one(query)
    except UniqueViolation:
        raise HTTPException(status_code=500)
    return NotesOutSchema.from_orm(note_obj)


async def delete_note(note_id: int):
    query = delete(Notes).where(Notes.id == note_id)
    try:
        await database.execute(query)
    except Exception as e:
        print("\n\n")
        print(e)
        print("\n\n")
    return Status(message="success")
