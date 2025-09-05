from sqlalchemy import and_
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.myapp.models.ItemCarrinho import ItemCarrinho
from src.myapp.schemas.CarrinhoSchema import CarrinhoSchema
from src.myapp.schemas.CarrinhoSchema import ItemCarrinhoSchema
from src.myapp.models.Ferramenta import Ferramenta
from src.myapp.schemas.FerramentaSchema import FerramentaPreviewSchema

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

def mapper_ferramenta_preview(ferramenta: Ferramenta) -> ItemCarrinhoSchema:
    preview = FerramentaPreviewSchema(id=ferramenta.id, nome=ferramenta.nome, 
                                   diaria=ferramenta.diaria, categoria=ferramenta.categoria)
    

    return ItemCarrinhoSchema(ferramenta= preview)


def buscarCarrinho(idUsuario: int, secao:Session) -> CarrinhoSchema:
    itensCarrinho_model = secao.query(ItemCarrinho).filter(ItemCarrinho.id_usuario == idUsuario)

    itensCarrinho_schema = list(map(lambda item: mapper_ferramenta_preview(item.ferramenta), itensCarrinho_model))

    return CarrinhoSchema(ferramentas=itensCarrinho_schema)


def excluirFerramentaCarrinho(id_usuario: int, id_ferramenta:int, secao: Session):

    item = secao.query(ItemCarrinho).filter(and_(ItemCarrinho.id_usuario == id_usuario, 
                                                          ItemCarrinho.id_ferramenta == id_ferramenta)).first()
    
    if item:
        secao.delete(item)
        secao.commit()

        

def limparCarrinho(id_usuario: int, secao: Session):
    secao.query(ItemCarrinho).filter(ItemCarrinho.id_usuario == id_usuario).delete()

    secao.commit()
    