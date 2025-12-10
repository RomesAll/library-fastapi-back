from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import MetaData, ForeignKey, text
from datetime import datetime, timezone

def get_time_update() -> datetime:
    return datetime.now(tz=timezone.utc)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: datetime = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: datetime = mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=get_time_update)
    metadata = MetaData()

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    def __repr__(self):
        cols = []
        for key in self.__table__.columns.keys():
            cols.append(f'{key}={getattr(self, key)}')
        return f'{self.__class__.__name__} {', '.join(cols)}'