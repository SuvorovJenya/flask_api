from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordBearer
from utils.get_current_db import get_db
from schemas.TruckSchemas import TruckSchemas
from schemas.TransportSchemas import TransportSchemas
from service.TransportService import (
    get_transport_item,
    get_transport_by_id,
    create_transport,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
truck_router = APIRouter()


@truck_router.get("/truck", response_model=List[TruckSchemas])
def get(
    db: Session = Depends(get_db),
    args: TransportSchemas = Depends(),
):
    return get_transport_item(
        db,
        args=args,
        model_type='TRUCK',
    )


@truck_router.get("/truck/{id}", response_model=TruckSchemas)
def get_one(
        id: int,
        db: Session = Depends(get_db),
):
    truck = get_transport_by_id(db, id=id, model_type='TRUCK')
    if truck is None:
        raise HTTPException(status_code=404, detail="Truck not found")
    return truck


@truck_router.post("/truck")
def create_truck(
        item: TruckSchemas,
        db: Session = Depends(get_db),
):
    return create_transport(db=db, item=item, model_type='TRUCK')
