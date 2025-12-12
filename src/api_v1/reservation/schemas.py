from pydantic import BaseModel, Field
from datetime import datetime

class ReservationsPOSTSchemas(BaseModel):
    client_id: int = Field(default=None, ge=1, description='Id пользователя(клиента)')
    book_id: int = Field(default=None, ge=1, description='Id книги')
    count_books: int = Field(default=None, ge=1, le=50, description='Кол-во забронированных книг')
    booking_before: datetime = Field(default=None, description='Бронирование до')

class ReservationsGETSchemas(ReservationsPOSTSchemas):
    id: int
    created_at: datetime
    updated_at: datetime

class ReservationsPATCHSchemas(ReservationsPOSTSchemas):
    id: int

class ReservationsRelSchemas(ReservationsGETSchemas):
    distribution: "DistributionGETSchemas"