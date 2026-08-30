from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel
from datetime import date
from BancoDeDados.models import Cliente, Produto, engine, salvar_cliente_banco, buscar_cliente_banco, salvar_produto_banco
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()



app.mount("/static/clientes", StaticFiles(directory="InterfaceWeb/Clientes/static"), name="cliente_static")
app.mount("/static/produtos", StaticFiles(directory="InterfaceWeb/Produtos/static"), name="produto_static")

templates = Jinja2Templates(directory="InterfaceWeb")

SQLModel.metadata.create_all(engine)


@app.get("/clientes", response_class=HTMLResponse)
async def pagina_clientes(request: Request):
    return templates.TemplateResponse(
        request=request, name="Clientes/clientes.html", context={}
    )

@app.post("/clientes/registrar")
async def criar_cliente(cliente: Cliente):
    return salvar_cliente_banco(cliente)


@app.get("/produtos", response_class=HTMLResponse)
async def pagina_produtos(request: Request):
    return templates.TemplateResponse(
        request=request, name="Produtos/produtos.html", context={}
    ) 

@app.post("/produtos/clientes")
async def criar_cliente(produto: Produto):
    return salvar_produto_banco(produto)


@app.get("/produtos/clientes")
async def buscar_cliente(nome:str):
    if nome:
        return buscar_cliente_banco(nome)