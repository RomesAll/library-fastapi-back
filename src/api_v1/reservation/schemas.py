from pydantic import BaseModel
from datetime import datetime

class ReservationsPOSTSchemas(BaseModel):
    client_id: int
    book_id: int
    count_books: int
    booking_before: datetime

class ReservationsGETSchemas(ReservationsPOSTSchemas):
    id: int
    created_at: datetime
    updated_at: datetime

class ReservationsPATCHSchemas(BaseModel):
    client_id: int | None = None
    book_id: int | None = None
    count_books: int | None = None
    booking_before: datetime | None = None

class ReservationsRelSchemas(ReservationsGETSchemas):
    distribution: "DistributionGETSchemas"