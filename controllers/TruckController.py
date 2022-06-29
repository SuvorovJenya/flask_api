from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordBearer
from utils.get_current_db import get_db
from schemas.TruckSchema import TruckSchema
from schemas.TransportSchema import TransportSchema
from database.enums.TransportType import TransportType
from service.TransportService import (
    get_transport,
    get_transport_by_id,
    create_transport,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
truck_router = APIRouter()


@truck_router.get("/truck", response_model=List[TruckSchema])
def get(
    db: Session = Depends(get_db),
    args: TransportSchema = Depends(),
):
    return get_transport(
        db,
        args=args,
        type=TransportType['TRUCK'],
    )


@truck_router.get("/truck/{id}", response_model=TruckSchema)
def get_one(
        id: int,
        db: Session = Depends(get_db),
):
    truck = get_transport_by_id(db, id=id, type=TransportType['TRUCK'])
    if truck is None:
        raise HTTPException(status_code=404, detail="Truck not found")
    return truck


@truck_router.post("/truck")
def create_truck(
        item: TruckSchema,
        db: Session = Depends(get_db),
):
    return create_transport(db=db, item=item, type=TransportType['TRUCK'])
