from typing import Optional
from pydantic import BaseModel


class AutoSchema(BaseModel):
    id: Optional[int]
    model: str
    year_of_production: int
    mileage: int
    body_type: str
    color: str
    price: int
    complete_set: str

    class Config:
        orm_mode = True
