from app.database import engine
from sqlmodel import Session, select, SQLModel
from app.models.clientes import Cliente
        
def buscar_dados_banco(nome: str):
    with Session(engine) as session:
        from app.models.clientes import Cliente
        statement = select(Cliente).where(Cliente.nome_completo.contains(nome))
        resultados = session.exec(statement).all()

def buscar_cpf(cpf: str):
    with Session(engine) as session:
        from app.models.clientes import Cliente
        statement = select(Cliente).where(Cliente.cpf == cpf)
        resultados = session.exec(statement).all()
        for r in resultados:
           return r.cpf

def limpar_e_recriar_banco():
    from sqlalchemy import text
    with engine.begin() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE;"))
        conn.execute(text("CREATE SCHEMA public;"))
    SQLModel.metadata.create_all(engine)
    print("Banco de dados limpo e recriado com sucesso!")