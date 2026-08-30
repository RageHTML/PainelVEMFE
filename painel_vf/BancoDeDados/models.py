import os
from typing import Annotated
from datetime import date
from fastapi import Depends
from dotenv_vault import load_dotenv
from sqlmodel import Field, SQLModel, create_engine, Session, select

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)


class Cliente(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome_completo: str = Field()
  nome_mae: str | None = Field()
  cpf: str = Field(unique=True)
  data_nascimento: date = Field()
  endereco: str | None = Field()


class Produto(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  cliente_id: int | None = Field(default=None, foreign_key="cliente.id")
  descricao: str | None = Field(default=None)
  valor: float = Field()
  forma_pagamento: str | None = Field()
  status: str = Field(default="pendente")
  data_pedido: date = Field(default_factory=date.today)
  data_entregue: date | None = Field()

def salvar_cliente_banco(cliente: Cliente):
    with Session(engine) as session:
      session.add(cliente)
      session.commit()
      session.refresh(cliente)
      return cliente

def salvar_produto_banco(produto: Produto):
    with Session(engine) as session:
      session.add(produto)
      session.commit()
      session.refresh(produto)
      return produto
    
    
def buscar_cliente_banco(nome: str):
    with Session(engine) as session:
        statement = (
            select(Cliente)
            .where(Cliente.nome_completo.ilike(f"%{nome}%"))
            .limit(5)
        )
        return session.exec(statement).all() 


