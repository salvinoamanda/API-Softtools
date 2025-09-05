from sqlalchemy.orm import Session
from sqlalchemy import select, and_, or_
from src.myapp.models.Ferramenta import Ferramenta
from src.myapp.models.Ferramenta import StatusFerramenta
from src.myapp.models.Usuario import Usuario
from src.myapp.schemas.FerramentaSchema import FerramentaSchema
from typing import List

def string_to_status(status: str):
    if status == StatusFerramenta.DISPONIVEL.name:
        return StatusFerramenta.DISPONIVEL
    
    return StatusFerramenta.ALUGADA

def readFerramentas(secao: Session, uf: str | None, status : str | None = None) -> List[FerramentaSchema]:

    statement = select(Ferramenta).join(Ferramenta.proprietario).where(and_(or_(Usuario.estado == uf, uf is None), 
                                                                            or_(Ferramenta.status == string_to_status(status), status is None)))
 

    ferramentas = secao.scalars(statement).all()

    return list(map(lambda ferramenta: FerramentaSchema(
        id = ferramenta.id,
        nome = ferramenta.nome,
        diaria = ferramenta.diaria,
        descricao = ferramenta.descricao,
        status = ferramenta.status,
        categoria = ferramenta.categoria,
        chave_pix = ferramenta.chave_pix,
        avaliacao = ferramenta.avaliacao,
        quantidade_avaliacoes = ferramenta.quantidade_avaliacoes,
        id_proprietario = ferramenta.id_proprietario,
    ) , ferramentas))