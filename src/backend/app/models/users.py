from app.models.base import BaseModel, Column
from app.models.mixins import IdMixin, TsMixinCreated, TsMixinUpdated
from sqlalchemy import PrimaryKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import Mapped


class User(BaseModel, IdMixin, TsMixinCreated, TsMixinUpdated):
    __tablename__ = "users"

    __table_args__ = (PrimaryKeyConstraint("id", name="user_pkey"),)

    username: Mapped[str] = Column(String(127), nullable=False, init=False)
    full_name: Mapped[str] = Column(String(127), nullable=True, init=False)

    password: Mapped[str] = Column(String(127), nullable=False, init=False)

    UniqueConstraint(username, name='username_uniq')
