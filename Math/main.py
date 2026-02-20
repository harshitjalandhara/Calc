from fastapi import FastAPI
from src.Math.api.endpoints import router

app = FastAPI(title="Math")

app.include_router(router)