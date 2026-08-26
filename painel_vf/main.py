from fastapi import FastAPI,Form
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from sqlmodel import SQLModel
from datetime import date
from BancoDeDados.models import Cliente,Produto, engine
from pydantic import BaseModel


app = FastAPI()

app.frontend("/", directory="InterfaceWeb")
app.mount("/static", StaticFiles(directory="InterfaceWeb/static"), name="static")

SQLModel.metadata.create_all(engine)


class Cliente(BaseModel):
  nome_completo: str 
  nome_mae: str | None
  cpf: str  
  data_nascimento: date 
  endereco: str | None 


class Produto(BaseModel):
  cliente_id: int | None 
  descricao: str | None 
  valor: float
  forma_pagamento: str | None
  status: str | None = "pendente"
  data_entregue: date | None


@app.post("/clientes")
async def criar_cliente(cliente: Annotated[Cliente, Form()]):
    return cliente

@app.post("/produtos")
async def criar_produto(produto: Produto):
    return Produto
