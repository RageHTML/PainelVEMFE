from sqlmodel import Session, select, Field, SQLModel, Relationship
from fastapi import Request
from app.database import engine
from datetime import date

class Produto(SQLModel, table=True):
    __tablename__ = "produto"

    id: int | None = Field(default=None, primary_key=True)
    descricao: str | None = Field(default=None)
    contratos: list["Contratos"] = Relationship(back_populates="produto")


async def salvar_produto_banco(request: Request):
    data = await request.json()
    
    print(data)
    with Session(engine) as session:
        db_produto = Produto.model_validate(data)
        session.add(db_produto)
        session.commit()
        session.refresh(db_produto)
        return db_produto

