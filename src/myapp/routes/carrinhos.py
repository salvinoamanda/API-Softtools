from fastapi import APIRouter, Depends
from sqlalchemy import Session
from src.myapp.database import get_session
from src.myapp.security import auth_validation, getPayload
from src.myapp.services.carrinho import adicionarItem

carrinho_router = APIRouter(prefix="/carrinho")


@carrinho_router.post("/{id_ferramenta}")
def adicionar_ao_carrinho(id_ferramenta: int, secao: Session = Depends(get_session), token: str = Depends(auth_validation)):
    payload = getPayload(token)
    idUsuario = payload["id"]
    adicionarItem(idUsuario, id_ferramenta, secao)

