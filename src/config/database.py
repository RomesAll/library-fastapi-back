from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .project_config import settings

engine = create_async_engine(url=settings.database.DATABASE_URL_async, echo=True)
session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)