from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy.sql import select, delete
from sqlalchemy.exc import SQLAlchemyError
from psycopg2.errors import UniqueViolation

from dataclasses import dataclass

from fastapi import HTTPException, status

DEFAULT_LIMIT = 50


@dataclass
class BaseCRUD:
    db_session: Session
    model = None

    def create(self, instance: Any):
        try:
            self.db_session.add(instance)
            self.db_session.commit()
            self.db_session.refresh(instance)
            return instance
        except SQLAlchemyError as error:
            print(error)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def find(self, **kwargs: Any) -> Any:
        stmt = select(self.model).filter_by(**kwargs)
        result = self.db_session.execute(stmt)
        instance = result.scalars().first()
        return instance

    def delete(self, **kwargs: Any) -> Any:
        stmt = delete(self.model).filter_by(**kwargs)
        try:
            self.db_session.execute(stmt)
            self.db_session.commit()
        except SQLAlchemyError as error:
            print("ERRROR =", error)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get_list(
        self, *, limit: int = DEFAULT_LIMIT, offset: int = 0, **kwargs: Any
    ) -> list[Any]:
        stmt = select(self.model).filter_by(**kwargs).offset(offset).limit(limit)
        print(stmt)
        result = self.db_session.execute(stmt)
        return result.scalars().all()

    @classmethod
    def delete2(cls, db_session: Session, **kwargs: Any) -> None:
        stmt = delete(cls).where(**kwargs)
        try:
            db_session.execute(stmt)
            db_session.commit()
        except SQLAlchemyError as error:
            print("ERRROR =", error)
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
