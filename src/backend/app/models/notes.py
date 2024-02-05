from __future__ import annotations

import uuid

from app.models.base import BaseModel, Column, RestrictForeignKey
from app.models.mixins import IdMixin, TsMixinCreated, TsMixinUpdated
from app.models.users import User
from sqlalchemy import PrimaryKeyConstraint, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, relationship


class Note(BaseModel, IdMixin, TsMixinCreated, TsMixinUpdated):
    __tablename__ = "notes"

    __table_args__ = (PrimaryKeyConstraint("id", name="note_pkey"),)

    content: Mapped[str] = Column(Text, nullable=True)
    author_id: Mapped[uuid.UUID] = Column(
        UUID(as_uuid=True),
        RestrictForeignKey(User.id),
        nullable=False,
    )

    author: Mapped[User] = relationship("User", lazy="noload")
