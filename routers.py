from fastapi import APIRouter
from autos import router

api_routers = APIRouter()
api_routers.include_router(router)
