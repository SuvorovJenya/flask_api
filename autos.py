
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List, Optional, Union
from jose import jwt
import models
import schemas
import crud


models.Base.metadata.create_all(bind=engine)

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "4e384a89b51013619805bf82acdb089c6b832ebf90aac1161aca3aecc8960030"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/autos", response_model=List[schemas.AutoModel])
def get(
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
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db),
):
    return crud.create(db=db, item=item)


def get_user(
    username: str,
    db: Session = Depends(get_db),
):
    return db.query(models.UserModel).\
        filter(models.UserModel.username == username).first()


def authenticate_user(
    username: str,
    password: str,
    db: Session = Depends(get_db),
):
    user = get_user(db, username)
    if not user:
        return False
    return user


def create_access_token(
    data: dict,
    expires_delta: Union[timedelta, None] = None,
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
