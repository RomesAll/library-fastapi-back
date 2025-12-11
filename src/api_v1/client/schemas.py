from pydantic import BaseModel
from datetime import datetime

class ClientPOSTSchemas(BaseModel):
    username: str
    first_name: str
    second_name: str
    address: str
    is_active: bool
    phone_number: str
    password: bytes

class ClientGETSchemas(ClientPOSTSchemas):
    id: int
    created_at: datetime
    updated_at: datetime

class ClientPATCHSchemas(BaseModel):
    username: str | None = None
    first_name: str | None = None
    second_name: str | None = None
    address: str | None = None
    is_active: bool | None = None
    phone_number: str | None = None

class ClientRelSchemas(ClientGETSchemas):
    clients: list["BookGETSchemas"]