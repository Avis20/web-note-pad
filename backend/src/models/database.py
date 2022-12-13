# ./backend/models/database.py
"""
Модуль для работы с БД
"""
import logging
import sys
from typing import Generator

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

from fastapi import HTTPException

from src.settings import get_settings

settings = get_settings()

if settings.DB_ECHO_LOG:
    logger = logging.StreamHandler(sys.stdout)
    logger_sa = logging.getLogger("sqlalchemy")
    logger_sa.setLevel(logging.INFO)
    logger_sa.addHandler(logger)

engine = sa.create_engine(
    settings.db_master_uri,
    echo=True,
)
metadata = sa.MetaData()
Base = declarative_base(metadata=metadata)

sync_session = sessionmaker(bind=engine, autocommit=False, autoflush=True)


def db_session() -> Generator:
    with sync_session() as session:
        try:
            yield session
            session.commit()
        except SQLAlchemyError as sql_ex:
            print("AAAAAAAAA SQLAlchemyError:rollback")
            session.rollback()
            raise sql_ex
        except HTTPException as http_ex:
            print("AAAAAAAAA HTTPException:rollback")
            session.rollback()
            raise http_ex
        finally:
            print("COMMMMMIIIITTTT")
            session.close()
