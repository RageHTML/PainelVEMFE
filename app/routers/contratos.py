from datetime import datetime
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from app.main import templates

import re 
router = APIRouter()



@router.get("/festas", response_class=HTMLResponse)
def exibir_pagina_contrato(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="festas.html",
        context={"pagina_atual": "festas"},
        status_code=200
    )

@router.get("/festas/buscar_festas", response_class=HTMLResponse)
async def pagina_produtos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="buscar_festas.html",
        context={"pagina_atual": "produtos"},
        status_code=200
    )

@router.post("/clientes/contratos/criar")
async def criar_contrato(request: Request):
    from app.models.contratos import criar_contrato
    from app.models.clientes import buscar_id_cliente
    data = await request.json()
    id_cliente = buscar_id_cliente(data.get("nome_completo"))
    forma_pagamento = data.get("forma_pagamento")
    data_entregue = data.get("data_entregue")
    valor = int(data.get("valor"))
    return criar_contrato(id_cliente, valor, forma_pagamento, data_entregue)

@router.post("/clientes/contratos/buscar")
async def todos_contratos(request: Request):
  from app.models.contratos import retornar_contratos
  data = await request.json()
  q = data.get("busca")
  return retornar_contratos(q)

@router.post("/clientes/contratos/gerar_contrato")
async def gerar(request: Request):
  from app.models.contratos import gerar_contrato

  campos_dict = await request.json()
  chave_campos = campos_dict.keys()

  for c in chave_campos:
      campo = re.sub("_", " ", c)
      conteudo_campo = campos_dict[f'{c}']

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