
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List, Optional
import models
import schemas
import crud


models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/autos", response_model=List[schemas.AutoModel])
def get_autos(
        db: Session = Depends(get_db),
        model: Optional[str] = None,
        year_of_production: Optional[int] = None,
        mileage: Optional[str] = None,
        body_type: Optional[str] = None,
        color: Optional[str] = None,
        price: Optional[int] = None,
        ):
    return crud.get(
        db,
        model=model,
        year_of_production=year_of_production,
        mileage=mileage,
        body_type=body_type,
        color=color,
        price=price,
        )


@router.get("/autos/{auto_id}", response_model=schemas.AutoModel)
def get_by_id(
        auto_id: int,
        db: Session = Depends(get_db),
        ):
    db_user = crud.get_by_id(db, auto_id=auto_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/autos")
def create(
        item: schemas.AutoModel,
        db: Session = Depends(get_db),
        ):
    return crud.create(db=db, item=item)
