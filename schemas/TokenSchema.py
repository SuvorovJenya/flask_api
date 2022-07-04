from typing import Union
from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str


class TokenDataSchema(BaseModel):
    username: Union[str, None] = None
