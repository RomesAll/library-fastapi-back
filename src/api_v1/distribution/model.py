from config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime

class DistributionsORM(Base):
    reservation_id: Mapped[int] = mapped_column(ForeignKey('reservationsorm.id', ondelete='CASCADE'))
    distribution_date: Mapped[datetime]
    return_date: Mapped[datetime]
    reservation: Mapped["ReservationsORM"] = relationship(back_populates='distribution', uselist=False)
