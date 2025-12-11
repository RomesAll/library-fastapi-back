from config import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ClientsORM(Base):
    username: Mapped[str] = mapped_column(unique=True) # Попробовать другой способ с динамич. сосзданием
    first_name: Mapped[str]
    second_name: Mapped[str | None]
    address: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False)
    phone_number: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] # = mapped_column(hash=True)
    
    client_books: Mapped[list["BooksORM"]] = relationship(back_populates='', secondary='reservationsorm')

    def __init__(self, first_name, second_name, **kw):
        super().__init__(first_name=first_name, second_name=second_name, **kw)
        self.full_name = f'{first_name} {second_name}'