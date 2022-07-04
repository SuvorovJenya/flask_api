from typing import Optional
from pydantic import BaseModel


class TransportSchema(BaseModel):
    model: Optional[str]
    year_of_production: Optional[int]
    body_type: Optional[str]
    color: Optional[str]
    price: Optional[int]
    complete_set: Optional[str]
    cylinders: Optional[int]
    tacts: Optional[int]
    lifting_capacity: Optional[int]
    suspension_chassis: Optional[str]
    wheel_arrangement: Optional[int]

    class Config:
        orm_mode = True
