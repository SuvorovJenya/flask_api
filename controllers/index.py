from fastapi import APIRouter
from autos import router

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


api_routers = APIRouter()
api_routers.include_router(router)
