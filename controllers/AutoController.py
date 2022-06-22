from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi.security import OAuth2PasswordBearer
from database.models.AutoModel import AutoModel
from utils.get_current_db import get_db
from schemas.AutoSchemas import AutoSchemas
from service.TransportService import get_transport_item, get_transport_by_id, create_transport


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
auto_router = APIRouter()


@auto_router.get("/autos", response_model=List[AutoSchemas])
def get(
    db: Session = Depends(get_db),
    model: Optional[str] = None,
    year_of_production: Optional[int] = None,
    mileage: Optional[str] = None,
    body_type: Optional[str] = None,
    color: Optional[str] = None,
    price: Optional[int] = None,
    complete_set: Optional[int] = None,
):
    return get_transport_item(
        db,
        model=model,
        year_of_production=year_of_production,
        mileage=mileage,
        body_type=body_type,
        color=color,
        price=price,
        complete_set=complete_set,
        table_name=AutoModel,
    )


@auto_router.get("/autos/{id}", response_model=AutoSchemas)
def get_one(
        id: int,
        db: Session = Depends(get_db),
):
    auto = get_transport_by_id(db, id=id, table_name=AutoModel)
    if auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    return auto


@auto_router.post("/autos")
def create_auto(
        item: AutoSchemas,
        db: Session = Depends(get_db),
):
    return create_transport(db=db, item=item, table_name=AutoModel)
