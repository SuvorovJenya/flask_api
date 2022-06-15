from fastapi import FastAPI
from controllers.index import api_routers
from database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_routers)
