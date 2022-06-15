from typing import Union
from pydantic import BaseModel


class TokenSchemas(BaseModel):
    access_token: str


class TokenDataSchemas(BaseModel):
    username: Union[str, None] = None
