from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from fastapi.responses import FileResponse
from src.myapp.database import get_session
from src.myapp.security import auth_validation, getPayload
from sqlalchemy.orm import Session
from src.myapp.schemas.FerramentaSchema import FerramentaComFotosSchema, FerramentaSchema, FerramentaCadastroSchema, AvaliacaoSchema, FerramentaAtualizacaoSchema
from typing import List
from decimal import Decimal
from src.myapp.services.ferramentas import readFerramentas, readFerramenta, createNovaFerramenta, atualizaFerramenta, avaliar, busca_foto
from src.myapp.services.ferramentas import excluirFerramenta

ferramentas_router = APIRouter(prefix="/ferramentas")

#Endpoints de ferramentas

@ferramentas_router.get("/", response_model= List[FerramentaComFotosSchema])
def getFerramentas(uf: str | None = None, status: str | None = None , 
                   secao: Session = Depends(get_session), _: str = Depends(auth_validation)):
    
    return readFerramentas(secao, uf, status)

@ferramentas_router.get("/{id}", response_model= FerramentaComFotosSchema)
def getFerramenta(id: int, 
                   secao: Session = Depends(get_session), _: str = Depends(auth_validation)):
    
    return readFerramenta(id, secao)

@ferramentas_router.post("/")
async def createFerramenta(nome: str = Form(...),
                     diaria: Decimal = Form(...),
                     descricao: str = Form(...),
                     categoria: str = Form(...),
                     chave_pix: str = Form(...),
                     quantidade_estoque: int = Form(1),
                     fotos: List[UploadFile] = File(default_factory=list),
                     secao: Session = Depends(get_session), 
                     token: str = Depends(auth_validation)):


    idUsuario = getPayload(token)["id"]

    dadosNovaFerramenta = FerramentaCadastroSchema(nome=nome,
                                                   diaria=diaria,
                                                   descricao=descricao,
                                                   categoria=categoria,
                                                   chave_pix=chave_pix,
                                                   quantidade_estoque=quantidade_estoque,
                                                   fotos=fotos)

    return await createNovaFerramenta(dadosNovaFerramenta, idUsuario, secao)

@ferramentas_router.patch("/", response_model=FerramentaSchema, status_code=status.HTTP_202_ACCEPTED)
def att_ferramenta(dadosFerramenta: FerramentaAtualizacaoSchema, secao: Session = Depends(get_session), token: str = Depends(auth_validation)):
    idUsuario = getPayload(token)["id"]

    return atualizaFerramenta(idUsuario, dadosFerramenta, secao)

@ferramentas_router.post("/avaliar", response_model=FerramentaSchema, status_code=status.HTTP_202_ACCEPTED)
def avaliar_ferramenta(avaliacaoDados: AvaliacaoSchema, 
                       secao: Session = Depends(get_session), 
                       _: str = Depends(auth_validation)):

   return avaliar(avaliacaoDados, secao)

@ferramentas_router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def excluir_ferramenta(idFerramenta: int,
                       secao: Session = Depends(get_session),
                       _: str = Depends(auth_validation)):
    excluirFerramenta(idFerramenta, secao)


@ferramentas_router.get("/foto/{id_foto}")
def get_foto(id_foto: int, 
             secao: Session = Depends(get_session), 
             _: str = Depends(auth_validation)) -> FileResponse:
    
    return busca_foto(id_foto, secao)
