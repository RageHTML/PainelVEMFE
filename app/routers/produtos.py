from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from app.main import templates
from app.models.produtos import Produto, salvar_produto_banco
router = APIRouter()

@router.get("/produtos", response_class=HTMLResponse)
async def pagina_produtos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="produtos.html",
        context={"pagina_atual": "produtos"},
        status_code=200
    )


@router.post("/produtos/registrar")
async def criar_produto(produto: Produto):
    return salvar_produto_banco(produto)


