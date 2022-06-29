from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[int]
    username: str
    password: str

    class Config:
        orm_mode = True
