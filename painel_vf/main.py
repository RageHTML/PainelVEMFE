from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel
from datetime import date
from BancoDeDados.models import Cliente, Produto, engine, salvar_cliente_banco
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()



app.mount("/static", StaticFiles(directory="InterfaceWeb/static"), name="static")
templates = Jinja2Templates(directory="InterfaceWeb")

SQLModel.metadata.create_all(engine)


@app.get("/clientes", response_class=HTMLResponse)
async def pagina_clientes(request: Request):
    return templates.TemplateResponse(
        request=request, name="clientes.html", context={}
    )

@app.post("/clientes/registrar")
async def criar_cliente(cliente_data: Cliente):
    return salvar_cliente_banco(cliente_data)

@app.post("/produtos")
async def criar_produto(produto: Produto):
    return produto 