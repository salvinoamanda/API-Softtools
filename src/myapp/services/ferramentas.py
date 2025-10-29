from sqlalchemy.orm import Session
from sqlalchemy import select, and_, or_
from src.myapp.models.Ferramenta import Ferramenta, StatusFerramenta, CategoriaFerramenta
from src.myapp.models.Usuario import Usuario
from src.myapp.models.Foto import Foto
from src.myapp.schemas.FerramentaSchema import FerramentaSchema, FerramentaCadastroSchema, AvaliacaoSchema, FerramentaAtualizacaoSchema
from typing import List
from fastapi import status, HTTPException, UploadFile
import os, uuid

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


def readFerramenta(id: int, secao: Session) -> FerramentaSchema:

    statement = select(Ferramenta).where(Ferramenta.id == id)
 

    ferramentas = secao.scalars(statement).first()

    return FerramentaSchema(
        id = ferramentas.id,
        nome = ferramentas.nome,
        diaria = ferramentas.diaria,
        descricao = ferramentas.descricao,
        status = ferramentas.status,
        categoria = ferramentas.categoria,
        chave_pix = ferramentas.chave_pix,
        avaliacao = ferramentas.avaliacao,
        quantidade_avaliacoes = ferramentas.quantidade_avaliacoes,
        id_proprietario = ferramentas.id_proprietario,
        quantidade_estoque= ferramentas.quantidade_estoque
    )


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


async def registrarFotos(fotos: List[UploadFile], secao: Session, id_ferramenta: int):
    os.makedirs("Fotos", exist_ok=True)

    for foto in fotos:

        raw = await foto.read()

        ext = {"image/webp": "webp", "image/png": "png", "image/jpeg": "jpg"}[foto.content_type]

        nova_foto = Foto(id_ferramenta=id_ferramenta)

        secao.add(nova_foto)
        secao.flush()
        id_gerado = nova_foto.id

        filename = f"{id_gerado}.{ext}"

        path = os.path.join("Fotos", filename)

        with open(path, "wb") as out:
            out.write(raw)
    
    secao.commit()

        
    

def createNovaFerramenta(dados: FerramentaCadastroSchema, fotos: List[UploadFile], id_propietario:int, secao: Session):

    novaFerramenta = Ferramenta(nome=dados.nome, diaria=dados.diaria,descricao=dados.descricao,
               categoria=str_to_categoria(dados.categoria),chave_pix=dados.chave_pix,id_proprietario=id_propietario,
               quantidade_estoque=dados.quantidade_estoque)
    
    secao.add(novaFerramenta)

    registrarFotos(fotos, secao)

    secao.commit()

    return status.HTTP_201_CREATED

def atualizaFerramenta(id_usuario: int, dadosFerramenta: FerramentaAtualizacaoSchema, secao: Session) -> FerramentaSchema:

    ferramenta = secao.query(Ferramenta).filter(dadosFerramenta.id_ferramenta == Ferramenta.id).first()

    if ferramenta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ferramenta não encontrada.")


    if ferramenta.id_proprietario != id_usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não autorizado para alterar esta ferramenta.")
    

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

    secao.commit()
    secao.refresh(ferramenta)
    

    return FerramentaSchema(id = ferramenta.id,
                            nome = ferramenta.nome,
                            diaria = ferramenta.diaria,
                            descricao = ferramenta.descricao,
                            status = ferramenta.status,
                            categoria = ferramenta.categoria,
                            chave_pix = ferramenta.chave_pix,
                            avaliacao=ferramenta.avaliacao,
                            quantidade_avaliacoes=ferramenta.quantidade_avaliacoes,
                            id_proprietario= ferramenta.id_proprietario,
                            quantidade_estoque = ferramenta.quantidade_estoque)

def avaliar(dadosAvaliacao: AvaliacaoSchema, secao: Session):

    ferramenta = secao.query(Ferramenta).filter(Ferramenta.id == dadosAvaliacao.id_ferramenta).first()

    if ferramenta is None:
        HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Ferramenta não encontrada.")


    nova_avaliacao = ((ferramenta.quantidade_avaliacoes * ferramenta.avaliacao) + dadosAvaliacao.avaliacao) / (ferramenta.quantidade_avaliacoes + 1)
    
    ferramenta.quantidade_avaliacoes += 1

    ferramenta.avaliacao = nova_avaliacao

    secao.commit()
    secao.refresh(ferramenta)

    return FerramentaSchema(id = ferramenta.id,
                            nome = ferramenta.nome,
                            diaria = ferramenta.diaria,
                            descricao = ferramenta.descricao,
                            status = ferramenta.status,
                            categoria = ferramenta.categoria,
                            chave_pix = ferramenta.chave_pix,
                            avaliacao=ferramenta.avaliacao,
                            quantidade_avaliacoes=ferramenta.quantidade_avaliacoes,
                            id_proprietario= ferramenta.id_proprietario,
                            quantidade_estoque = ferramenta.quantidade_estoque)

# Busca ferramenta por ID
def buscaFerramentaPorID(id: int, secao: Session) -> Ferramenta | None:

    try:
        ferramenta = secao.scalar(select(Ferramenta).where(Ferramenta.id == id))
        if not ferramenta:   
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ferramenta não encontrada")
        return ferramenta
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Falha ao consultar o banco de dados.")

# Função para excluir ferramenta
def excluirFerramenta(idFerramenta: int, secao: Session):
    ferramenta = buscaFerramentaPorID(idFerramenta, secao)

    secao.delete(ferramenta)
    secao.commit()