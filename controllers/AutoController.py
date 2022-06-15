from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi.security import OAuth2PasswordBearer
from utils.get_current_db import get_db
from schemas.AutoSchemas import AutoSchemas
from service.AutoService import get_auto_item, get_by_id, create


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
):
    return get_auto_item(
        db,
        model=model,
        year_of_production=year_of_production,
        mileage=mileage,
        body_type=body_type,
        color=color,
        price=price,
    )


@auto_router.get("/autos/{auto_id}", response_model=AutoSchemas)
def get_one(
        auto_id: int,
        db: Session = Depends(get_db),
):
    auto = get_by_id(db, auto_id=auto_id)
    if auto is None:
        raise HTTPException(status_code=404, detail="Auto not found")
    return auto


@auto_router.post("/autos")
def create_auto(
        item: AutoSchemas,
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db),
):
    return create(db=db, item=item)
