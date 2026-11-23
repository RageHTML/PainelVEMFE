from sqlmodel import Session, select, Field, SQLModel, Relationship
from fastapi import Request, HTTPException
from typing import Optional
from app.database import engine
from datetime import date
from app.models.contratos import Contratos
class Festa(SQLModel, table=True):
    __tablename__ = "festa"

    id: int | None = Field(default=None, primary_key=True)
    descricao: str | None = Field(default=None)
    endereco: str | None = Field(default=None)
    numero: str | None = Field(default=None)
    bairro: str  | None = Field(default=None)
    contrato_id: int | None = Field(default=None, foreign_key="contratos.id")
    contrato: Optional["Contratos"] = Relationship(back_populates="festa")

def criar_festa(contrato: Contratos, contrato_id: int, descricao: str):
    try:  
        with Session(engine) as session:
            festa = Festa(contrato=contrato, contrato_id=contrato_id, descricao=descricao)
            session.add(festa)
            session.commit()
            session.refresh(festa)
    except Exception as e:
        erro = str(e).replace("\n", "").strip()
        print(erro)

   

