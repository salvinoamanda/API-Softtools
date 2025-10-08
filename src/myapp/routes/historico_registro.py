from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.myapp.database import get_session
from src.myapp.security import auth_validation, getPayload
from myapp.services.historico import historico_registro

historico_registro_router = APIRouter(prefix="/historico_registro", tags=["Historico do Registro"])

@historico_registro_router.get("/")
def visualizar_historico_registro(sessao: Session = Depends(get_session), token: str = Depends(auth_validation)):
    payload = getPayload(token)
    idUsuario = payload["id"]

    return historico_registro(id_usuario=idUsuario, sessao=sessao)