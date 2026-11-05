from sqlmodel import Session, select, Field, SQLModel, Relationship
from typing import Optional
from app.database import engine
from datetime import date

class Contratos(SQLModel, table=True):
    __tablename__ = "contratos"

    id: int | None = Field(default=None, primary_key=True)
    id_cliente: int | None = Field(default=None, foreign_key="cliente.id")
    id_produto: int | None = Field(default=None, foreign_key="produto.id")

    cliente: Optional["Cliente"] = Relationship(back_populates="contratos")
    produto: Optional["Produto"] = Relationship(back_populates="contratos")

    valor: float
    forma_pagamento: str | None = Field(default=None)
    status: str = Field(default="pendente")
    data_pedido: date = Field(default_factory=date.today)
    data_entregue: date | None = Field(default=None)