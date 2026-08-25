from fastapi import FastAPI
from sqlmodel import SQLModel
from BancoDeDados.models import Cliente,Produto, engine


app = FastAPI()


SQLModel.metadata.create_all(engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}
