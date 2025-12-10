from config import Base
from sqlalchemy.orm import Mapped, mapped_column

class ClientsORM(Base):
    first_name: Mapped[str]
    second_name: Mapped[str | None]
    address: Mapped[str]

    def __init__(self, first_name, second_name, **kw):
        super().__init__(first_name=first_name, second_name=second_name, **kw)
        self.full_name = f'{first_name} {second_name}'