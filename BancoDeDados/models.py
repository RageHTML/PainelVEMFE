import os
from typing import Annotated
from datetime import date
from fastapi import Depends,Response, HTTPException, Request
from dotenv_vault import load_dotenv
from sqlmodel import Field, SQLModel, create_engine, Session, select
import re

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)


class Cliente(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome_completo: str = Field()
  nome_mae: str = Field()
  cpf: str = Field(unique=True)
  data_nascimento: date = Field()
  endereco: str = Field()

class Produto(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  cliente_id: int | None = Field(default=None, foreign_key="cliente.id")
  descricao: str | None = Field(default=None)
  valor: float = Field()
  forma_pagamento: str | None = Field()
  status: str = Field(default="pendente")
  data_pedido: date = Field(default_factory=date.today)
  data_entregue: date | None = Field()

async def salvar_cliente_banco(request: Request, cliente: Cliente ):
    campos_dict = await request.json()
    chave_campos = campos_dict.keys()

    for c in chave_campos:
       campo = re.sub("_", " ", c)
       conteudo_campo = campos_dict[f'{c}'].strip()

       if conteudo_campo == "":
          raise HTTPException(detail=f"O campo {campo} está vazio.",status_code=422)
       elif len(conteudo_campo) < 3:
          raise HTTPException (detail=f"quantidade de caracteres de {campo} isuficiente", status_code=400)
       
    try:  
      with Session(engine) as session:
        db_cliente = cliente.model_validate(cliente)
        session.add(db_cliente)
        session.commit()
        session.refresh(db_cliente)
        return db_cliente
    except Exception as e:
        erro = str(e).replace("\n", "").strip()
        if "validation error for Clientedata_nascimento" in erro: 
          raise HTTPException(detail="Data de nascimento precisa ser preenchida", status_code =400)
        else:
          raise HTTPException(detail=f"{erro}", status_code =400)
      
def buscar_cliente_banco(nome: str):
    with Session(engine) as session:
        statement = select(Cliente).where(Cliente.nome.contains(nome))
        resultados = session.exec(statement).all()
        return resultados


def salvar_produto_banco(produto: Produto):
    with Session(engine) as session:
        session.add(produto)
        session.commit()
        session.refresh(produto)
        return produto

