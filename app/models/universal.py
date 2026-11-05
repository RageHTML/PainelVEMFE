from app.database import engine
from sqlmodel import Session, select


def buscar_cliente_banco(nome: str):
    with Session(engine) as session:
        from app.models.clientes import Cliente
        statement = select(Cliente).where(Cliente.nome_completo.contains(nome))
        resultados = session.exec(statement).all()
        for r in resultados:
           return r.nome_completo
        
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