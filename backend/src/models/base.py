from typing import Any
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Session
from sqlalchemy.sql import select, delete
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status


@as_declarative()
class BaseModel:
    def save(self, db_session: Session):
        try:
            db_session.add(self)
            db_session.commit()
            db_session.refresh(self)
            return self
        except SQLAlchemyError as error:
            print("ERRROR =", error)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @classmethod
    def delete(cls, db_session: Session, id: Any):
        stmt = delete(cls).where(cls.id == id)
        try:
            db_session.execute(stmt)
            db_session.commit()
        except SQLAlchemyError as error:
            print("ERRROR =", error)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @classmethod
    def find(cls, db_session: Session, field: str, value: Any):
        stmt = select(cls).where(getattr(cls, field) == value)
        result = db_session.execute(stmt)
        instance = result.scalars().first()
        return instance

    

