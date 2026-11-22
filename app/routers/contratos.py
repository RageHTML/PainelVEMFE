

from fastapi import APIRouter, Request, HTTPException
import re 
router = APIRouter()

@router.post("/contratos/buscar")
async def todos_contratos(request: Request):
  from app.models.contratos import retornar_contratos
  data = await request.json()
  q = data.get("busca")
  return retornar_contratos(q)

@router.post("/contratos/gerar")
async def gerar(request: Request):
  from app.models.contratos import gerar_contrato

  campos_dict = await request.json()
  chave_campos = campos_dict.keys()

  for c in chave_campos:
      campo = re.sub("_", " ", c)
      conteudo_campo = campos_dict[f'{c}']

      print(campo, conteudo_campo)

      if conteudo_campo is None:
        raise HTTPException(detail=f"o {campo} esta vazio, e preciso prenechelo editando", status_code=422)
        
  gerar_contrato(
    campos_dict.get("nome_completo"), 
    campos_dict.get("cpf"), 
    campos_dict.get("data_entregue"),
    campos_dict.get("endereco"),
    campos_dict.get("numero"),
    campos_dict.get("valor"),
    campos_dict.get("forma_pagamento"),
    campos_dict.get("status")
    )

  raise HTTPException(detail="sucesso", status_code=200)