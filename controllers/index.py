from fastapi import APIRouter
from controllers.AuthController import auth_router
from controllers.AutoController import auto_router
from controllers.TruckController import truck_router
from controllers.MotoController import moto_router


api_routers = APIRouter()
api_routers.include_router(auth_router)
api_routers.include_router(auto_router)
api_routers.include_router(truck_router)
api_routers.include_router(moto_router)
