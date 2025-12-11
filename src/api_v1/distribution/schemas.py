from pydantic import BaseModel
from datetime import datetime

class DistributionPOSTSchemas(BaseModel):
    reservation_id: int
    distribution_date: datetime
    return_date: datetime

class DistributionGETSchemas(DistributionPOSTSchemas):
    id: int
    created_at: datetime
    updated_at: datetime

class DistributionPATCHSchemas(BaseModel):
    reservation_id: int | None = None
    distribution_date: datetime | None = None
    return_date: datetime | None = None

class DistributionRelSchemas(DistributionGETSchemas):
    reservation: "ReservationsGETSchemas"