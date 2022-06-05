
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
def read_autos(
        db: Session = Depends(get_db),
        color: Optional[str] = None,
        ):
    if color:
        return crud.get_autos(db, color)
    else:
        return crud.get_autos(db)


@router.get("/autos/{auto_id}", response_model=schemas.AutoModel)
def read_auto_one(
        auto_id: int,
        db: Session = Depends(get_db),
        ):
    db_user = crud.get_autos_one(db, auto_id=auto_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/autos")
def create_item_for_auto(
        item: schemas.AutoModel,
        db: Session = Depends(get_db),
        ):
    return crud.create_auto(db=db, item=item)
