from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.myapp.database import get_session
from src.myapp.security import auth_validation, getPayload
from src.myapp.services.carrinho import adicionarItem, buscarCarrinho, excluirFerramentaCarrinho, limparCarrinho
from src.myapp.schemas.CarrinhoSchema import CarrinhoSchema

carrinho_router = APIRouter(prefix="/carrinho")


@carrinho_router.post("/{id_ferramenta}")
def adicionar_ao_carrinho(id_ferramenta: int, secao: Session = Depends(get_session), token: str = Depends(auth_validation)):
    payload = getPayload(token)
    idUsuario = payload["id"]
    adicionarItem(idUsuario, id_ferramenta, secao)

@carrinho_router.get(path="/",response_model=CarrinhoSchema)
def vizualizar_carrinho(secao: Session = Depends(get_session), token: str = Depends(auth_validation)):
    payload = getPayload(token)
    idUsuario = payload["id"]
    carrinho = buscarCarrinho(idUsuario, secao)
    return carrinho


@carrinho_router.delete(path="/delete/{id_item}")
def deletar_item_carrinho(id_item:int, secao: Session = Depends(get_session), token: str = Depends(auth_validation)):
    payload = getPayload(token)
    idUsuario = payload["id"]

    excluirFerramentaCarrinho(idUsuario, id_item, secao)


@carrinho_router.delete(path="/")
def limpar_carrinho(secao: Session = Depends(get_session), token: str = Depends(auth_validation)):
    payload = getPayload(token)
    idUsuario = payload["id"]

    limparCarrinho(idUsuario, secao)