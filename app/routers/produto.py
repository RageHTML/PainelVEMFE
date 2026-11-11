from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from app.main import templates
router = APIRouter()

@router.get("/produtos", response_class=HTMLResponse)
async def pagina_produtos(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="produto_busca.html",
        context={"pagina_atual": "produtos"},
        status_code=200
    )



