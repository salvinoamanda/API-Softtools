from fastapi import APIRouter, Depends
from typing import List
from src.myapp.schemas.HistoricoSchema import ItemHistoricoSchema
from src.myapp.security import auth_validation, getPayload
from src.myapp.services.historico import readHistoricoAlugueis
from sqlalchemy.orm import Session
from src.myapp.database import get_session

historico_router = APIRouter(prefix="/historico")

@historico_router.get("/", response_model= List[ItemHistoricoSchema])
def getHistoricoAlugueis(token: str = Depends(auth_validation), secao: Session = Depends(get_session)):
    idUsuario = getPayload(token)["id"]
    return readHistoricoAlugueis(idUsuario, secao)

