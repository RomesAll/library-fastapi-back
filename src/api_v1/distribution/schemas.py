from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException, status

class DistributionPOSTSchemas(BaseModel):
    reservation_id: int = Field(default=0, description='Id бронирования')
    distribution_date: datetime = Field(default=None, description='Дата выдачи книги')
    return_date: datetime = Field(default=None, description='Дата возврата книги')

    @model_validator(mode='after')
    def validate_datetime(self, data):
        if self.distribution_date > self.return_date:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Date is not correct')
        return data

class DistributionGETSchemas(DistributionPOSTSchemas):
    id: int
    created_at: datetime
    updated_at: datetime

class DistributionPATCHSchemas(DistributionPOSTSchemas):
    id: int

class DistributionRelSchemas(DistributionGETSchemas):
    reservation: "ReservationsGETSchemas"