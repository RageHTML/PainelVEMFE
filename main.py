from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel

from BancoDeDados.models import engine
from app.routes import router

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.mount("/static", StaticFiles(directory="InterfaceWeb"), name="static")

app.include_router(router)
