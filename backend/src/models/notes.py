# ./backend/models/notes.py

"""
Модель хранения заметок
"""

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from src.models.database import BaseModel


class Notes(BaseModel):

    __tablename__ = "notes"

    id = sa.Column(
        sa.Integer,
        primary_key=True,
        comment="ID Заметки")
    title = sa.Column(
        sa.String(256),
        nullable=False,
        comment="Заголовок заметки")
    content = sa.Column(
        sa.Text,
        nullable=True,
        comment="Содержание заметки")

    author_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("users.id"),
        nullable=False,
        comment="ID автора заметки")

    author = relationship("Users", back_populates="notes")
