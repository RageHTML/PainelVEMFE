

from fastapi import APIRouter, Request, HTTPException
import re 
router = APIRouter()

@router.post("/contratos/buscar")
async def todos_contratos(request: Request):
  from app.models.contratos import retornar_contratos
  data = await request.json()
  q = data.get("busca")
  return retornar_contratos(q)

@router.post("/contratos/gerar")
def gerar(request: Request):
  from app.models.contratos import gerar_contrato
  gerar_contrato(request)
  raise HTTPException(detail="sucesso", status_code=200)