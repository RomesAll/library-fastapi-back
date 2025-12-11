from config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime

class ReservationsORM(Base):
    client_id: Mapped[int] = mapped_column(ForeignKey('clientsorm.id', ondelete='CASCADE'))
    book_id: Mapped[int] = mapped_column(ForeignKey('booksorm.id', ondelete='CASCADE'))
    count_books: Mapped[int]
    booking_before: Mapped[datetime]
    distribution: Mapped["DistributionsORM"] = relationship(back_populates='reservation', uselist=False)