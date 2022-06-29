from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordBearer
from utils.get_current_db import get_db
from database.enums.TransportType import TransportType
from schemas.AutoSchema import AutoSchema
from schemas.TransportSchema import TransportSchema
from service.TransportService import (
    get_transport,
    get_transport_by_id,
    create_transport,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
auto_router = APIRouter()


@auto_router.get("/autos", response_model=List[AutoSchema])
def get(
    db: Session = Depends(get_db),
    args: TransportSchema = Depends(),
):
    return get_transport(
        db,
        args=args,
        type=TransportType['AUTOS'],
    )


@auto_router.get("/autos/{id}", response_model=AutoSchema)
def get_one(
        id: int,
        db: Session = Depends(get_db),
):
    auto = get_transport_by_id(db, id=id, type=TransportType['AUTOS'])
    if auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    return auto


@auto_router.post("/autos")
def create_auto(
        item: AutoSchema,
        db: Session = Depends(get_db),
):
    return create_transport(db=db, item=item, type=TransportType['AUTOS'])
