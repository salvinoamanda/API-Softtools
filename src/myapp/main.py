from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from src.myapp.routes.ferramentas import ferramentas_router
from src.myapp.routes.usuarios import usuarios_router
from src.myapp.routes.aluguel import aluguel_router
from src.myapp.routes.carrinhos import carrinho_router
from src.myapp.routes.historico import historico_router
from src.myapp.routes.historico_registro import historico_registro_router


#Instancia da API
app = FastAPI()

#Carrega a URL do front e libera pro front acessar a API
load_dotenv()
URL_FRONT = os.getenv("URL_FRONT")
origins = [URL_FRONT]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

#Define as rotas da API puxando da pasta router
app.include_router(ferramentas_router)
app.include_router(usuarios_router)
app.include_router(aluguel_router)
app.include_router(carrinho_router)
app.include_router(historico_router)
app.include_router(historico_registro_router)