from sqlalchemy import and_
from sqlalchemy.orm import Session
from src.myapp.models.ItemCarrinho import ItemCarrinho
from src.myapp.schemas.CarrinhoSchema import CarrinhoSchema
from src.myapp.schemas.CarrinhoSchema import ItemCarrinhoSchema
from src.myapp.models.Ferramenta import Ferramenta
from src.myapp.schemas.FerramentaSchema import FerramentaPreviewSchema

def adicionarItem(id_usuario:int, id_item: int, secao: Session):

    item = secao.query(ItemCarrinho).filter(and_(ItemCarrinho.id_usuario == id_usuario, 
                                                          ItemCarrinho.id_ferramenta == id_item)).first()
    
    if item:
        item.quantidade += 1
    else:
        item = ItemCarrinho(id_usuario=id_usuario, id_ferramenta=id_item)

    secao.add(item)
    secao.commit()
    secao.refresh(item)


    return item

def mapper_ferramenta_preview(ferramenta: Ferramenta, quantidadeItem: int) -> ItemCarrinhoSchema:
    preview = FerramentaPreviewSchema(id=ferramenta.id, nome=ferramenta.nome, 
                                   diaria=ferramenta.diaria, categoria=ferramenta.categoria)
    
    valorTotalDiaria = ferramenta.diaria * quantidadeItem

    return ItemCarrinhoSchema(ferramenta= preview, quantidade=quantidadeItem, valorTotalDiaria=valorTotalDiaria)


def buscarCarrinho(idUsuario: int, secao:Session) -> CarrinhoSchema:
    itensCarrinho_model = secao.query(ItemCarrinho).filter(ItemCarrinho.id_usuario == idUsuario)

    itensCarrinho_schema = list(map(lambda item: mapper_ferramenta_preview(item.ferramenta, item.quantidade), itensCarrinho_model))

    valoresPreliminares = list(map(lambda preview: preview.valorTotalDiaria, itensCarrinho_schema))

    return CarrinhoSchema(ferramentas=itensCarrinho_schema, valorTotalPreliminar= sum(valoresPreliminares))


        