from sqlmodel import Field, SQLModel, create_engine, Session, select
from fastapi import Depends,Response, HTTPException, Request
from dotenv_vault import load_dotenv
from typing import Annotated
from datetime import date
import re
import os

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"), echo=True)


class Cliente(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome_completo: str = Field()
  nome_mae: str = Field()
  cpf: str = Field(unique=True)
  data_nascimento: date = Field()
  endereco: str = Field()

class Produto(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  cliente_id: int | None = Field(default=None, foreign_key="cliente.id")
  descricao: str | None = Field(default=None)
  valor: float = Field()
  forma_pagamento: str | None = Field()
  status: str = Field(default="pendente")
  data_pedido: date = Field(default_factory=date.today)
  data_entregue: date | None = Field()

def buscar_cpf(cpf: str):
    with Session(engine) as session:
        statement = select(Cliente).where(Cliente.cpf == cpf)
        resultados = session.exec(statement).first()
        return resultados
        
async def salvar_cliente_banco(request: Request, cliente: Cliente):
   campos_dict = await request.json()
   chave_campos = campos_dict.keys()

   for c in chave_campos:
      campo = re.sub("_", " ", c)
      conteudo_campo = campos_dict[f'{c}']

      if c == "cpf":
         limpo = re.sub(r"\D","", conteudo_campo).lower()
         campos_dict[c] = limpo
         resultados = buscar_cpf(limpo)

         if len(limpo) != 11:
            raise HTTPException(detail=f"O campo {campo} deve conter exatamente 11 dígitos.", status_code=422)
         elif resultados != None:
            raise HTTPException(detail="Este CPF já está cadastrado no sistema.", status_code=422)
      elif c == "nome_completo" or c == "nome_mae":
         limpo = " ".join(conteudo_campo.split()).lower()
         campos_dict[c] = limpo
         if len (limpo) < 3:
            raise HTTPException(detail=f"O campo {campo} deve conter ao menos 3 caracteres.", status_code=422)
      elif c == "endereco":
         limpo = " ".join(conteudo_campo.split()).lower()
         campos_dict[c] = limpo
      
          
      if conteudo_campo == "":
         raise HTTPException(detail=f"O campo {campo} não pode estar vazio.", status_code=422)
      elif len(conteudo_campo) < 3:
         raise HTTPException (detail=f"A quantidade de caracteres no campo {campo} é insuficiente.", status_code=400)
       
   try:  
      with Session(engine) as session:
         db_cliente = cliente.model_validate(campos_dict)
         session.add(db_cliente)
         session.commit()
         session.refresh(db_cliente)
         return db_cliente
   except Exception as e:
      erro = str(e).replace("\n", "").strip()
      print(erro)
      
def buscar_cliente_banco(nome: str):
    with Session(engine) as session:
        statement = select(Cliente).where(Cliente.nome_completo.contains(nome))
        resultados = session.exec(statement).all()
        for r in resultados:
           print(r.nome_completo)

        return resultados



def salvar_produto_banco(produto: Produto):
    with Session(engine) as session:
        session.add(produto)
        session.commit()
        session.refresh(produto)
        return produto

