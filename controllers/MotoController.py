from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi.security import OAuth2PasswordBearer
from database.models.MotoModel import MotoModel
from utils.get_current_db import get_db
from schemas.MotoSchemas import MotoSchemas
from service.TransportService import get_transport_item, get_transport_by_id, create_transport

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
moto_router = APIRouter()


@moto_router.get("/moto", response_model=List[MotoSchemas])
def get(
    db: Session = Depends(get_db),
    model: Optional[str] = None,
    year_of_production: Optional[int] = None,
    mileage: Optional[str] = None,
    body_type: Optional[str] = None,
    color: Optional[str] = None,
    price: Optional[int] = None,
    cylinders: Optional[int] = None,
    tacts: Optional[int] = None,
):
    return get_transport_item(
        db,
        model=model,
        year_of_production=year_of_production,
        mileage=mileage,
        body_type=body_type,
        color=color,
        price=price,
        cylinders=cylinders,
        tacts=tacts,
        table_name=MotoModel,
    )


@moto_router.get("/moto/{id}", response_model=MotoSchemas)
def get_one(
        id: int,
        db: Session = Depends(get_db),
):
    moto = get_transport_by_id(db, id=id, table_name=MotoModel)
    if moto is None:
        raise HTTPException(status_code=404, detail="Moto not found")
    return moto


@moto_router.post("/moto")
def create_moto(
        item: MotoSchemas,
        db: Session = Depends(get_db),
):
    return create_transport(db=db, item=item, table_name=MotoModel)
