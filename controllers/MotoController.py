from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordBearer
from utils.get_current_db import get_db
from schemas.MotoSchemas import MotoSchemas
from schemas.TransportSchemas import TransportSchemas
from service.TransportService import (
    get_transport_item,
    get_transport_by_id,
    create_transport,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
moto_router = APIRouter()


@moto_router.get("/moto", response_model=List[MotoSchemas])
def get(
    db: Session = Depends(get_db),
    args: TransportSchemas = Depends(),
):
    return get_transport_item(
        db,
        args=args,
        model_type='MOTO',
    )


@moto_router.get("/moto/{id}", response_model=MotoSchemas)
def get_one(
        id: int,
        db: Session = Depends(get_db),
):
    moto = get_transport_by_id(db, id=id, model_type='MOTO')
    if moto is None:
        raise HTTPException(status_code=404, detail="Moto not found")
    return moto


@moto_router.post("/moto")
def create_moto(
        item: MotoSchemas,
        db: Session = Depends(get_db),
):
    return create_transport(db=db, item=item, model_type='MOTO')
