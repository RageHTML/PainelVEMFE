from sqlmodel import Session, select, Field, SQLModel, Relationship
from fastapi import Request, HTTPException
from typing import Optional
from app.database import engine
from datetime import date

class Produto(SQLModel, table=True):
    __tablename__ = "produto"

    id: int | None = Field(default=None, primary_key=True)
    descricao: str | None = Field(default=None)
    
    contrato_id: int | None = Field(default=None, foreign_key="contratos.id")
    contrato: Optional["Contratos"] = Relationship(back_populates="produtos")


def salvar_descricao(descricao: str, id: str):
    db_produto = Produto(descricao=f"{descricao}")
    with Session(engine) as session:
        session.add(db_produto)
        session.commit()
        session.refresh(db_produto)
    return HTTPException(detail="sucesso", status_code="200")


async def salvar_produto_banco(request: Request):
    campos_dict = await request.json()
    chave_campos = campos_dict.keys()
    from app.models.clientes import buscar_id_cliente
    for c in chave_campos:
        conteudo = campos_dict[f'{c}']

        if c == "nome_completo":
            id_cliente = buscar_id_cliente(conteudo)
        elif c == "descricao":
            salvar_descricao(conteudo, id_cliente)
        else:
         with Session(engine) as session:
            db_produto = Produto.model_validate(data)
            session.add(db_produto)
            session.commit()
            session.refresh(db_produto)
            return db_produto

   

