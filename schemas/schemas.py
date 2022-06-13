from typing import Optional, Union
from pydantic import BaseModel


class AutoSchema(BaseModel):
    id: Optional[int]
    model: str
    year_of_production: int
    mileage: int
    body_type: str
    color: str
    price: int

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    id: Optional[int]
    username: str
    password: str


class TokenSchema(BaseModel):
    access_token: str


class TokenPayloadSchema(BaseModel):
    id: Union[str, None] = None
