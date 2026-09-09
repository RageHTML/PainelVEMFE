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

@router.get("/clientes", response_class=HTMLResponse)
async def pagina_clientes(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/clientes/index.html",
        context={"active_page": "clientes"}
    )

@router.post("/clientes/registrar")
async def criar_cliente(cliente: Cliente):
    return salvar_cliente_banco(cliente)

@router.get("/clientes/buscar")
async def buscar_cliente(nome: str):
    if nome:
        return buscar_cliente_banco(nome)

@router.get("/produtos", response_class=HTMLResponse)
async def pagina_produtos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/produtos/index.html",
        context={"active_page": "produtos"}
    )

@router.post("/produtos/registrar")
async def criar_produto(produto: Produto):
    return salvar_produto_banco(produto)