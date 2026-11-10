from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from app.main import templates
from app.models.produtos import Produto, salvar_produto_banco
router = APIRouter()

@router.get("/produtos", response_class=HTMLResponse)
async def pagina_produtos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="produto_busca.html",
        context={"pagina_atual": "produtos"},
        status_code=200
    )

@router.get("/produtos/novo", response_class=HTMLResponse)
async def pagina_produtos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="produto_novo.html",
        context={"pagina_atual": "produtos"},
        status_code=200
    )

@router.post("/produtos/registrar")
async def criar_produto(request: Request):
    return await salvar_produto_banco(request)


