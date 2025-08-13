from fastapi import APIRouter, Depends
from src.myapp.database import get_session
from src.myapp.security import auth_validation
from sqlalchemy.orm import Session
from src.myapp.schemas.FerramentaSchema import FerramentaSchema
from typing import List
from src.myapp.services.ferramentas import readFerramentas


ferramentas_router = APIRouter(prefix="/ferramentas")

#Endpoints de ferramentas

@ferramentas_router.get("/", response_model= List[FerramentaSchema])
def getFerramentas(uf: str | None = None, secao: Session = Depends(get_session), _: str = Depends(auth_validation)):
    return readFerramentas(secao, uf)