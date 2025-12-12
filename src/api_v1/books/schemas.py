from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime

class BookPOSTSchemas(BaseModel):
    name: str = Field(default='name', min_length=1, max_length=200, examples=['«Евгений Онегин»'], description='Названия книги')
    author: str = Field(default='author', min_length=2, max_length=50, examples=['Пушкин А.С.'], description='Автор книги')
    publishing: str = Field(default='publishing', min_length=1, max_length=100, examples=['«Академиздат».'], description='Издатель')
    year_publishing: int = Field(default=1980, ge=1980, le=2100, examples=['2001'], description='Год издания')
    count_pages: int = Field(default=10, ge=10, examples=['100'], description='Кол-во страниц')
    price: float = Field(default=10, ge=0, examples=['540'], description='Цена за книгу в руб.')
    count_books: int = Field(default=10, ge=0, examples=['80'], description='Кол-во книг')
    model_config = ConfigDict(from_attributes=True)

class BookGETSchemas(BookPOSTSchemas):
    id: int
    created_at: datetime
    updated_at: datetime

class BookPATCHSchemas(BookPOSTSchemas):
    id: int

class BookRelSchemas(BookGETSchemas):
    books: list["ClientGETSchemas"]