from sqlalchemy import and_
from sqlalchemy.orm import Session
from src.myapp.models.ItemCarrinho import ItemCarrinho

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


        