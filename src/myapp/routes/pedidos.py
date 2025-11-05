from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.myapp.database import get_session
from src.myapp.security import auth_validation, getPayload
from src.myapp.schemas.PedidoSchema import PedidoSchema
from src.myapp.services.pedidos import registraPagamento, registrarPedido


pedidos_router = APIRouter(prefix="/pedidos")

@pedidos_router.post("/", status_code= status.HTTP_201_CREATED)
def postPedidos(dadosPedido: PedidoSchema, secao: Session = Depends(get_session),
                token: str = Depends(auth_validation)):

    id_usuario = getPayload(token)["id"]
    return registrarPedido(dadosPedido, id_usuario, secao)

@pedidos_router.post("/pagar/{id_pedido}")
def pagar_pedido(id_pedido:int,
                 secao: Session = Depends(get_session),
                 token: str = Depends(auth_validation)):
    
    return registraPagamento(id_pedido, secao)