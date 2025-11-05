from sqlalchemy import and_
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.myapp.models.ItemCarrinho import ItemCarrinho
from src.myapp.schemas.CarrinhoSchema import CarrinhoSchema
from src.myapp.schemas.CarrinhoSchema import ItemCarrinhoSchema
from src.myapp.models.Ferramenta import Ferramenta
from src.myapp.models.Foto import Foto
from src.myapp.schemas.FerramentaSchema import FerramentaPreviewSchema
from typing import List


def adicionarItem(id_usuario:int, id_item: int, secao: Session):

    item = secao.query(ItemCarrinho).filter(and_(ItemCarrinho.id_usuario == id_usuario, 
                                                          ItemCarrinho.id_ferramenta == id_item)).first()
    
    if item:
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Este item já existe no carrinho.")
    else:
        item = ItemCarrinho(id_usuario=id_usuario, id_ferramenta=id_item)

    secao.add(item)
    secao.commit()
    secao.refresh(item)


    return item

def mapper_ferramenta_preview(ferramenta: Ferramenta, ids_fotos: List[int]) -> ItemCarrinhoSchema:
    preview = FerramentaPreviewSchema(id=ferramenta.id, nome=ferramenta.nome, 
                                   diaria=ferramenta.diaria, categoria=ferramenta.categoria,
                                   ids_foto=ids_fotos)
    

    return ItemCarrinhoSchema(ferramenta= preview)


def buscarCarrinho(idUsuario: int, secao:Session) -> CarrinhoSchema:
    itensCarrinho_model = secao.query(ItemCarrinho).filter(ItemCarrinho.id_usuario == idUsuario)

    schemas = []

    for item in itensCarrinho_model:
        fotos = secao.query(Foto).where(Foto.id_ferramenta == item.id_ferramenta)

        schema = mapper_ferramenta_preview(item.ferramenta, [foto.id for foto in fotos])

        schemas.append(schema)

    return CarrinhoSchema(ferramentas=schemas)


def excluirFerramentaCarrinho(id_usuario: int, id_ferramenta:int, secao: Session):

    item = secao.query(ItemCarrinho).filter(and_(ItemCarrinho.id_usuario == id_usuario, ItemCarrinho.id_ferramenta == id_ferramenta)).first()
    
    if item:
        secao.delete(item)
        secao.commit()

        

def limparCarrinho(id_usuario: int, secao: Session):
    secao.query(ItemCarrinho).filter(ItemCarrinho.id_usuario == id_usuario).delete()

    secao.commit()    