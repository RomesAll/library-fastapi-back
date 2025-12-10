from config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime

class ReservationsORM(Base):
    client_id: Mapped[int] = mapped_column(ForeignKey('clientsorm.id', ondelete='CASCADE'))
    book_id: Mapped[int] = mapped_column(ForeignKey('booksorm.id', ondelete='CASCADE'))
    booking_before: Mapped[datetime]
