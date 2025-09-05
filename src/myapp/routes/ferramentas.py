from fastapi import APIRouter, Depends
from src.myapp.database import get_session
from src.myapp.security import auth_validation, getPayload
from sqlalchemy.orm import Session
from src.myapp.schemas.FerramentaSchema import FerramentaSchema, FerramentaCadastroSchema, FerramentaAtualizacaoSchema
from typing import List
from src.myapp.services.ferramentas import readFerramentas, createNovaFerramenta, atualizaFerramenta


ferramentas_router = APIRouter(prefix="/ferramentas")

#Endpoints de ferramentas

@ferramentas_router.get("/", response_model= List[FerramentaSchema])
def getFerramentas(uf: str | None = None, status: str | None = None , 
                   secao: Session = Depends(get_session), _: str = Depends(auth_validation)):
    
    return readFerramentas(secao, uf, status)

@ferramentas_router.post("/")
def createFerramenta(dadosNovaFerramenta: FerramentaCadastroSchema, secao: Session = Depends(get_session), token: str = Depends(auth_validation)):

    idUsuario = getPayload(token)["id"]

    return createNovaFerramenta(dadosNovaFerramenta, idUsuario, secao)

@ferramentas_router.patch("/", response_model=FerramentaSchema)
def att_ferramenta(dadosFerramenta: FerramentaAtualizacaoSchema, secao: Session = Depends(get_session), token: str = Depends(auth_validation)):
    
    idUsuario = getPayload(token)["id"]

    return atualizaFerramenta(idUsuario, dadosFerramenta, secao)