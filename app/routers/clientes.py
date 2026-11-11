from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from app.main import templates

router = APIRouter()

@router.get("/clientes", response_class=HTMLResponse)
def pagina_clientes(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="clientes.html",
        context={"pagina_atual": "clientes"},
        status_code=200
    )


@router.post("/clientes/buscar")
async def buscar_cliente(request: Request):
    from app.models.clientes import buscar_nome_completo
    data = await request.json()
    nome = data.get("nome")
    return buscar_nome_completo(nome)

@router.post("/clientes")
async def criar_cliente(request: Request):
    from app.models.clientes import salvar_cliente_banco
    return await salvar_cliente_banco(request)
