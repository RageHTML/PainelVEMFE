from fastapi.responses import HTMLResponse
from datetime import datetime
from app.main import templates
from fastapi import APIRouter, Request
router = APIRouter()


@router.get("/festas", response_class=HTMLResponse)
def exibir_pagina_contrato(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="festas.html",
        context={"pagina_atual": "festas"},
        status_code=200
    )

@router.get("/festas/buscar", response_class=HTMLResponse)
async def pagina_produtos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="buscar_festas.html",
        context={"pagina_atual": "produtos"},
        status_code=200
    )

@router.post("/festas")
async def criar_festa(request: Request):
    from app.models.contratos import criar_contrato
    from app.models.clientes import buscar_id_cliente
    from app.models.universal import transformar_date
    data = await request.json()
    id_cliente = buscar_id_cliente(data.get("nome_completo"))
    valor = int(data.get("valor"))
    forma_pagamento = data.get("forma_pagamento")
    data_entregue = data.get("data_entregue")
    descricao = data.get("descricao")
    return criar_contrato(id_cliente, valor, forma_pagamento, data_entregue, descricao)
