import os
from datetime import date
from dotenv_vault import load_dotenv
from sqlmodel import Field, SQLModel, create_engine

load_dotenv()


class Cliente(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome_completo: str
  nome_mae: str | None = None
  cpf: str = Field(unique=True)
  data_nascimento: date
  endereco: str | None = None


class Produto(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  cliente_id: int | None = Field(default=None, foreign_key="cliente.id")
  descricao: str | None = None
  valor: int
  forma_pagamento: int
  status: str = Field(default="pendente")
  data_pedido: date = Field(default_factory=date.today)
  data_entregue: date | None = None


engine = create_engine(os.getenv("DATABASE_URL"), echo=True)