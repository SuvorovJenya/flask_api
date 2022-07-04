from fastapi import FastAPI
from controllers.index import api_routers
from database.db import Base, engine
from database.models.AutoModel import AutoModel
from database.models.MotoModel import MotoModel
from database.models.TruckModel import TruckModel

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_routers)
