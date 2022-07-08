# ./backend/models/notes.py

import sqlalchemy as sa

from src.models.database import BaseModel

class Note(BaseModel):
    __tablename__ = "notes"

    id = sa.Column(
        sa.Integer,
        primary_key=True
    ),
    name = sa.Column(
        sa.String(20),
        unique=True
    )
