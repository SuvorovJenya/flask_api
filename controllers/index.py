from fastapi import APIRouter
from controllers.AutoController import auto_router
from controllers.AuthController import auth_router


api_routers = APIRouter()
api_routers.include_router(auto_router)
api_routers.include_router(auth_router)
