import uuid

from app.models.base import BaseModel, Column, RestrictForeignKey
from app.models.mixins import IdMixin, TsMixinCreated, TsMixinUpdated
from app.models.users import User
from sqlalchemy import PrimaryKeyConstraint, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, relationship


class Note(BaseModel, IdMixin, TsMixinCreated, TsMixinUpdated):
    __tablename__ = "notes"

    title: Mapped[str] = Column(Text, nullable=False, init=False)
    content: Mapped[str] = Column(Text, nullable=True, init=False)
    author_id: Mapped[uuid.UUID] = Column(
        UUID(as_uuid=True),
        RestrictForeignKey(User.id),
        nullable=False,
        init=False,
    )

    author: Mapped[User] = relationship("User", lazy="noload", init=False)

    PrimaryKeyConstraint("id", name="note_pkey")
