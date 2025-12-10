from config import Base
from sqlalchemy.orm import Mapped, mapped_column

class BooksORM(Base):
    name: Mapped[str]
    author: Mapped[str]
    publishing: Mapped[str]
    year_publishing: Mapped[int]
    count_pages: Mapped[int]
    price: Mapped[float]
    count_books: Mapped[int]