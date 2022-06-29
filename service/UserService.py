import os
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from schemas.TokenSchema import TokenDataSchema
from database.models.UserModel import UserModel
from utils.get_current_db import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_user(
    username: str,
    db: Session,
):
    return db.query(UserModel).\
        filter_by(username=username).first()


def get_by_username(
    username: str,
    db: Session,
):
    user = get_user(db, username)
    if not user:
        return None
    return user


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            os.getenv('SECRET_KEY'),
            options={"verify_aud": False},
        )
        username: str = payload.get("userid")
        token_data = TokenDataSchema(username=username)
    except JWTError:
        raise credentials_exception
    user = db.query(UserModel).\
        filter(UserModel.id == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user
