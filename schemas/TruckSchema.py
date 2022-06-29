from typing import Optional
from pydantic import BaseModel


class TruckSchema(BaseModel):
    id: Optional[int]
    model: str
    year_of_production: int
    mileage: int
    body_type: str
    color: str
    price: int
    lifting_capacity: int
    suspension_chassis: str
    wheel_arrangement: int

    class Config:
        orm_mode = True
