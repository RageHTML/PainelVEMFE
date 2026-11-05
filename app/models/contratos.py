from sqlmodel import Session, select, Field, SQLModel, Relationship
from app.database import engine
from datetime import date

class Contratos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    id_cliente: int | None = Field(default=None, foreign_key="Cliente.id")
    id_produto: int | None = Field(default=None, foreign_key="Produto.id")

    cliente: "Cliente" | None = Relationship(back_populates="contratos")
    produto: "Produto" | None = Relationship(back_populates="contratos")

    valor: float = Field()
    forma_pagamento: str | None = Field()
    status: str = Field(default="pendente")
    data_pedido: date = Field(default_factory=date.today)
    data_entregue: date | None = Field()