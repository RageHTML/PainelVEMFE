from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from BancoDeDados.models import (
    Cliente,
    Produto,
    salvar_cliente_banco,
    buscar_cliente_banco,
    salvar_produto_banco,
)

router = APIRouter()
templates = Jinja2Templates(directory="InterfaceWeb")

@router.get("/contratos", response_class=HTMLResponse)
def exibir_pagina_contrato(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/contratos/index.html",
        context={"pagina_atual": "contratos"},
        status_code=200
    )
    
@router.get("/clientes", response_class=HTMLResponse)
def pagina_clientes(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/clientes/index.html",
        context={"pagina_atual": "clientes"},
        status_code=200
    )

@router.post("/clientes")
async def criar_cliente(cliente: Cliente):
    return salvar_cliente_banco(cliente)

@router.get("/produtos", response_class=HTMLResponse)
async def pagina_produtos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/produtos/index.html",
        context={"pagina_atual": "produtos"},
        status_code=200
    )

@router.get("/clientes/buscar")
async def buscar_cliente(nome: str):
    if nome:
        return buscar_cliente_banco(nome)

@router.post("/produtos/registrar")
async def criar_produto(produto: Produto):
    return salvar_produto_banco(produto)