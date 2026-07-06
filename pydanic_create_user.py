
from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    lastName: str = Field(alias="lastName")
    firstName: str = Field(alias="firstName")
    middleName: str = Field(alias="middleName")
    phoneNumber: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """
    Структура данных для создания нового пользователя.
    """
    email: EmailStr
    lastName: str = Field(alias="lastName")
    firstName: str = Field(alias="firstName")
    middleName: str = Field(alias="middleName")
    phoneNumber: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema