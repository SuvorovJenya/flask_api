from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi.security import OAuth2PasswordBearer
from database.models.TruckModel import TruckModel
from utils.get_current_db import get_db
from schemas.TruckSchemas import TruckSchemas
from service.TransportService import get_transport_item, get_transport_by_id, create_transport

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
truck_router = APIRouter()


@truck_router.get("/truck", response_model=List[TruckSchemas])
def get(
    db: Session = Depends(get_db),
    model: Optional[str] = None,
    year_of_production: Optional[int] = None,
    mileage: Optional[str] = None,
    body_type: Optional[str] = None,
    color: Optional[str] = None,
    price: Optional[int] = None,
    lifting_capacity: Optional[int] = None,
    suspension_chassis: Optional[str] = None,
    wheel_arrangement: Optional[int] = None,
):
    return get_transport_item(
        db,
        model=model,
        year_of_production=year_of_production,
        mileage=mileage,
        body_type=body_type,
        color=color,
        price=price,
        lifting_capacity=lifting_capacity,
        suspension_chassis=suspension_chassis,
        wheel_arrangement=wheel_arrangement,
        table_name=TruckModel,
    )


@truck_router.get("/truck/{id}", response_model=TruckSchemas)
def get_one(
        id: int,
        db: Session = Depends(get_db),
):
    truck = get_transport_by_id(db, id=id, table_name=TruckModel)
    if truck is None:
        raise HTTPException(status_code=404, detail="Truck not found")
    return truck


@truck_router.post("/truck")
def create_truck(
        item: TruckSchemas,
        db: Session = Depends(get_db),
):
    return create_transport(db=db, item=item, table_name=TruckModel)
