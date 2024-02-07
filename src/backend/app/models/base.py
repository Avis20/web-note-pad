from sqlalchemy import ForeignKey, MetaData
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column

Column = mapped_column

metadata = MetaData()


class BaseModel(DeclarativeBase, MappedAsDataclass):
    pass


class RestrictForeignKey(ForeignKey):
    def __init__(self, column, **dialect_kw):
        super().__init__(column, ondelete="CASCADE", onupdate="CASCADE", **dialect_kw)
