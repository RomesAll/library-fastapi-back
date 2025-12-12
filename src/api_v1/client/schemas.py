from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException, status
from datetime import datetime
import re

class ClientPOSTSchemas(BaseModel):
    username: str = Field(default='username', min_length=5, max_length=25, examples=['User1'], description='Username пользователя')
    first_name: str = Field(default='first_name', min_length=2, max_length=40, examples=['Петр'], description='Имя пользователя')
    second_name: str = Field(default='second_name', min_length=2, max_length=40, examples=['Петров'], description='Фамилия пользователя')
    address: str = Field(default='address', min_length=5, max_length=100, examples=['г. Москва ул. Пушкина д4 кв 183'], description='Адрес пользователя')
    phone_number: str = Field(default='+79021348299', examples=['+79021348299', '89021348299', '+7(902)134-82-99'], description='Телефон пользователя')
    email: str = Field(default='testemail@gmail.com', examples=['testemail@gmail.com'], description='Email пользователя')
    is_active: bool = Field(default=False, description='Активен ли пользователь')
    password: bytes = Field(default='testpassword', description='Пароль пользователя')

    @field_validator('phone_number')
    def validate_phone_number(cls, value):
        result = re.fullmatch(r'(\+7|8)([ ]?[-(]?\d{3}[)-]?[ ]?)([ ]?[-]?\d{3}[ ]?[-]?)([ -]?\d{2}[ -]?\d{2})', value)
        if result is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Phone number is not correct')
        return value

    @field_validator('email')
    def validate_email(cls, value):
        result = re.fullmatch(r'[a-z.0-9]+@[a-z]{2,10}\.[a-z]{2,5}', value)
        if result is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email is not correct')
        return value
    
class ClientGETSchemas(ClientPOSTSchemas):
    id: int
    created_at: datetime
    updated_at: datetime

class ClientPATCHSchemas(ClientPOSTSchemas):
    id: int

class ClientRelSchemas(ClientGETSchemas):
    clients: list["BookGETSchemas"]