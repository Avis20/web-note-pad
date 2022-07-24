# ./backend/models/notes.py

import sqlalchemy as sa

from src.models.database import BaseModel
from src.models.users import Users

class Notes(BaseModel):

    __tablename__ = "notes"

    id = sa.Column(
        sa.Integer,
        primary_key=True
    )
    title = sa.Column(
        sa.String(256),
        nullable=False,
    )
    content = sa.Column(
        sa.Text,
        nullable=True,
    )
    owner_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
