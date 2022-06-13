from typing import Optional, Union
from pydantic import BaseModel


class AutoModel(BaseModel):
    id: Optional[int]
    model: str
    year_of_production: int
    mileage: int
    body_type: str
    color: str
    price: int

    class Config:
        orm_mode = True


class UserModel(BaseModel):
    id: Optional[int]
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
