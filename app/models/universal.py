def buscar_cliente_banco(nome: str):
    with Session(engine) as session:
        statement = select(Cliente).where(Cliente.nome_completo.contains(nome))
        resultados = session.exec(statement).all()
        for r in resultados:
           return r.nome_completo
        
def buscar_dados_banco(nome: str):
    with Session(engine) as session:
        statement = select(Cliente).where(Cliente.nome_completo.contains(nome))
        resultados = session.exec(statement).all()
        for r in resultados:
           return r.nome_completo