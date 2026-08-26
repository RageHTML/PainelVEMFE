from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel
from datetime import date
from BancoDeDados.models import Cliente, Produto, engine, salvar_cliente_banco
from pydantic import BaseModel


app = FastAPI()

app.frontend("/", directory="InterfaceWeb")
app.mount("/static", StaticFiles(directory="InterfaceWeb/static"), name="static")

SQLModel.metadata.create_all(engine)


@app.post("/clientes")
async def criar_cliente(cliente_data: Cliente):
    return salvar_cliente_banco(cliente_data)

@app.post("/produtos")
async def criar_produto(produto: Produto):
    return produto 