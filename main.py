from fastapi import FastAPI
from routers import api_routers

app = FastAPI()
app.include_router(api_routers)
