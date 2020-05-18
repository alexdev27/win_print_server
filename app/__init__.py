from fastapi import FastAPI
from .datamax_oneil.routes import datamax_router

app = FastAPI()

app.include_router(datamax_router, prefix='/api', tags=['Print steakhouse order'])
