from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import MetaData, ForeignKey
from datetime import datetime

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: datetime = mapped_column()
    updated_at: datetime = mapped_column()
    metadata = MetaData()

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    def __repr__(self):
        cols = []
        for key in self.__table__.columns.keys():
            cols.append(f'{key}={getattr(self, key)}')
        return f'{self.__class__.__name__} {', '.join(cols)}'