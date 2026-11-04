from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from app.main import templates
from app.models.universal import buscar_cliente_banco
router = APIRouter()

@router.get("/contratos", response_class=HTMLResponse)
def exibir_pagina_contrato(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contratos.html",
        context={"pagina_atual": "contratos"},
        status_code=200
    )

@router.post("/contratos")
async def criar_contrato(request: Request):
    data = await request.json()
    nome = data.get("nome")
    return buscar_cliente_banco(nome)