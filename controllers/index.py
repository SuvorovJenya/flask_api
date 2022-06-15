from fastapi import APIRouter
from controllers.AuthController import auth_router
from controllers.AutoController import auto_router


api_routers = APIRouter()
api_routers.include_router(auth_router)
api_routers.include_router(auto_router)
