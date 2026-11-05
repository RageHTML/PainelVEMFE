from sqlmodel import Session, select, Field, SQLModel, Relationship
from app.database import engine
from datetime import date

class Produto(SQLModel, table=True):
    __tablename__ = "produto"

    id: int | None = Field(default=None, primary_key=True)
    descricao: str | None = Field(default=None)

    contratos: list["Contratos"] = Relationship(back_populates="produto")


def salvar_produto_banco(produto: Produto):
    with Session(engine) as session:
        session.add(produto)
        session.commit()
        session.refresh(produto)
        return produto

