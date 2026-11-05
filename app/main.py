from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.models.universal import limpar_e_recriar_banco
app = FastAPI()


templates = Jinja2Templates(directory="app/templates")
from app.routers import clientes, produtos, contratos, raiz
app.mount("/static", StaticFiles(directory="app/static"), name="static")



app.include_router(clientes.router)
app.include_router(produtos.router)
app.include_router(contratos.router)
app.include_router(raiz.router)