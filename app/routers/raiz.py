from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from app.main import templates
from app.models.universal import buscar_cliente_banco
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def exibir_pagina_contrato(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="raiz.html",
        context={"pagina_atual": "raiz"},
        status_code=200
    )