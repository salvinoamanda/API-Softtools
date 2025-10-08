from sqlalchemy.orm import Session
from sqlalchemy import select, and_, or_
from src.myapp.models.Ferramenta import Ferramenta, StatusFerramenta, CategoriaFerramenta
from src.myapp.models.Usuario import Usuario
from src.myapp.schemas.FerramentaSchema import FerramentaSchema, FerramentaCadastroSchema, FerramentaAtualizacaoSchema
from typing import List
from fastapi import status

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
        quantidade_estoque= ferramenta.quantidade_estoque
    ) , ferramentas))


def str_to_categoria(string: str):
    if string == 'MANUAL':
        return CategoriaFerramenta.MANUAL
    if string == 'ELETRICA':
        return CategoriaFerramenta.ELETRICA
    if string == 'PNEUMATICA':
        return CategoriaFerramenta.PNEUMATICA
    if string == 'HIDRAULICA':
        return CategoriaFerramenta.HIDRAULICA
    if string == 'MEDICAO':
        return CategoriaFerramenta.MEDICAO

    return None


def createNovaFerramenta(dados: FerramentaCadastroSchema, id_propietario:int, secao: Session):

    novaFerramenta = Ferramenta(nome=dados.nome, diaria=dados.diaria,descricao=dados.descricao,
               categoria=str_to_categoria(dados.categoria),chave_pix=dados.chave_pix,id_proprietario=id_propietario,
               quantidade_estoque=dados.quantidade_estoque)
    
    secao.add(novaFerramenta)
    secao.commit()

    return status.HTTP_201_CREATED

def atualizaFerramenta(id_usuario: int, dadosFerramenta: FerramentaAtualizacaoSchema, secao: Session) -> FerramentaSchema:

    ferramenta = secao.query(Ferramenta).filter(dadosFerramenta.id_ferramenta == Ferramenta.id).first()

    if ferramenta.id_proprietario != id_usuario:
        return status.HTTP_401_UNAUTHORIZED
    

    if dadosFerramenta.nome is not None:
        ferramenta.nome = dadosFerramenta.nome

    if dadosFerramenta.diaria is not None:
        ferramenta.diaria = dadosFerramenta.diaria

    if dadosFerramenta.descricao is not None:
        ferramenta.descricao = dadosFerramenta.descricao

    if dadosFerramenta.status is not None:
        ferramenta.status = string_to_status(dadosFerramenta.status)

    if dadosFerramenta.categoria is not None:
        ferramenta.categoria = str_to_categoria(dadosFerramenta.categoria)

    if dadosFerramenta.chave_pix is not None:
        ferramenta.chave_pix = dadosFerramenta.chave_pix

    if dadosFerramenta.quantidade_estoque is not None:
        ferramenta.quantidade_estoque = dadosFerramenta.quantidade_estoque

    return FerramentaSchema(id_ferramenta = ferramenta.id,
                            nome = ferramenta.nome,
                            diaria = ferramenta.diaria,
                            descricao = ferramenta.descricao,
                            status = ferramenta.status,
                            categoria = ferramenta.categoria,
                            chave_pix = ferramenta.chave_pix,
                            quantidade_estoque = ferramenta.quantidade_estoque)
