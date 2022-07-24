# ./backend/models/notes.py

import sqlalchemy as sa
from src.models.database import BaseModel

class Notes(BaseModel):

    __tablename__ = "notes"

    id = sa.Column(
        sa.Integer,
        primary_key=True
    )
    title = sa.Column(
        sa.Text(256),
    )