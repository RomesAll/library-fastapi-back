from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class BookPOSTSchemas(BaseModel):
    name: str
    author: str
    publishing: str 
    year_publishing: int
    count_pages: int
    price: float
    count_books: int
    model_config = ConfigDict(from_attributes=True)

class BookGETSchemas(BookPOSTSchemas):
    id: int
    created_at: datetime
    updated_at: datetime

class BookPATCHSchemas(BaseModel):
    name: str | None = None
    author: str | None = None
    publishing: str | None = None 
    year_publishing: int | None = None
    count_pages: int | None = None
    price: float | None = None
    count_books: int | None = None