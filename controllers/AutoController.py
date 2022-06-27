from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordBearer
from utils.get_current_db import get_db
from schemas.AutoSchemas import AutoSchemas
from schemas.TransportSchemas import TransportSchemas
from service.TransportService import (
    get_transport_item,
    get_transport_by_id,
    create_transport,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
auto_router = APIRouter()


@auto_router.get("/autos", response_model=List[AutoSchemas])
def get(
    db: Session = Depends(get_db),
    args: TransportSchemas = Depends(),
):
    return get_transport_item(
        db,
        args=args,
        model_type='AUTOS',
    )


@auto_router.get("/autos/{id}", response_model=AutoSchemas)
def get_one(
        id: int,
        db: Session = Depends(get_db),
):
    auto = get_transport_by_id(db, id=id, model_type='AUTOS')
    if auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    return auto


@auto_router.post("/autos")
def create_auto(
        item: AutoSchemas,
        db: Session = Depends(get_db),
):
    return create_transport(db=db, item=item, model_type='AUTOS')
