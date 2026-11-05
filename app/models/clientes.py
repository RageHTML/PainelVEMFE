from app.database import engine
from sqlmodel import Field, SQLModel, Session, Relationship
from fastapi import HTTPException, Request
from datetime import date
import re


class Cliente(SQLModel, table=True):
    __tablename__ = "cliente"

    id: int | None = Field(default=None, primary_key=True)
    nome_completo: str
    nome_mae: str
    cpf: str = Field(unique=True)
    data_nascimento: date
    endereco: str

    contratos: list["Contratos"] = Relationship(back_populates="cliente")


async def salvar_cliente_banco(request: Request):
   from app.models.universal import buscar_cpf
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
         db_cliente = Cliente.model_validate(campos_dict)
         session.add(db_cliente)
         session.commit()
         session.refresh(db_cliente)
         return db_cliente
   except Exception as e:
      erro = str(e).replace("\n", "").strip()
      print(erro)

