from typing import Annotated

from app.settings import Settings
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


class SQLAlchemyDatabase:
    def __init__(self):
        settings = Settings()
        engine = create_async_engine(
            settings.postgres.database_url,
            echo=settings.postgres.echo_log,
        )
        self.session_maker = async_sessionmaker(engine)

    def get_session_maker(self) -> async_sessionmaker[AsyncSession]:
        return self.session_maker


database_dep = SQLAlchemyDatabase()
SessionMakerDep = Annotated[
    async_sessionmaker[AsyncSession],
    Depends(database_dep.get_session_maker),
]
