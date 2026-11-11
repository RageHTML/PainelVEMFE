from sqlmodel import Session, select, Field, SQLModel, Relationship
from fastapi import HTTPException
from typing import Optional
from app.database import engine
from datetime import date

class Contratos(SQLModel, table=True):
    __tablename__ = "contratos"

    id: int | None = Field(default=None, primary_key=True)
    id_cliente: int | None = Field(default=None, foreign_key="cliente.id")

    cliente: Optional["Cliente"] = Relationship(back_populates="contratos")
    produtos: list["Produto"] = Relationship(back_populates="contrato")

    valor: float | None
    forma_pagamento: str | None = Field(default=None)
    status: str | None = Field(default="pendente")
    data_pedido: date | None = Field(default_factory=date.today)
    data_entregue: date | None = Field(default=None)

def buscar_contratos(nome: str):
    from app.models.clientes import buscar_id_cliente
    id_cliente = buscar_id_cliente(nome)
    with Session(engine) as session:
        statement = select(Contratos).where(Contratos.id_cliente == int(id_cliente))
        resultados = session.exec(statement).all()
        return resultados

def buscar_id_contrato(nome: str):
    from app.models.clientes import buscar_id_cliente
    id_cliente = buscar_id_cliente(nome)
    with Session(engine) as session:
        statement = select(Contratos).where(Contratos.id_cliente == int(id_cliente))
        resultados = session.exec(statement).all()
        for r in resultados:
            r.id_contrato
        return resultados

def criar_contrato(id_cliente: int, valor: int, forma_pagamento: str):
    try:  
        with Session(engine) as session:
            contrato = Contratos(id_cliente=f"{id_cliente}",valor=f"{valor}", forma_pagamento=f"{forma_pagamento}")
            session.add(contrato)
            session.commit()
            session.refresh(contrato)
            raise HTTPException(detail="Cliente cadastrado", status_code="200")
    except Exception as e:
        erro = str(e).replace("\n", "").strip()
        print(erro)