import settings
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.TokenSchemas import TokenSchemas
from schemas.UserSchemas import UserSchemas
from utils.create_access_token import create_access_token
from utils.get_current_db import get_db
from service.UserService import get_by_username, get_current_user
from database.models.UserModel import UserModel

auth_router = APIRouter()


@auth_router.post("/login", response_model=TokenSchemas)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = get_by_username(db, form_data.username)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    return {
        "access_token": create_access_token(userid=user.id),
        "token_type": "bearer",
    }


@auth_router.get("/me", response_model=UserSchemas)
def get_user_by_jwt(
    current_user: UserModel = Depends(get_current_user),
):
    user = current_user
    return user
