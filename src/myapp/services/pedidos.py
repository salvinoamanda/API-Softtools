from sqlalchemy.orm import Session
from src.myapp.models.Pedido import Pedido
from src.myapp.models.Ferramentas_pedido import Ferramentas_pedido
from src.myapp.schemas.PedidoSchema import PedidoSchema
from dotenv import load_dotenv
import os

load_dotenv()
CHAVE_PIX = os.getenv("CHAVE_PIX")

def registraPagamento(id_pedido: int, secao: Session):

    pedido : Pedido = secao.query(Pedido).where(Pedido.id == id_pedido).first()
    pedido.pago = True
    secao.commit()
    return {"pago": pedido.pago}

def registrarPedido(dados_pedido : PedidoSchema, id_usuario: int, secao: Session):
    novo_pedido = Pedido(id_solicitante=id_usuario,
                         quantidade_dias=dados_pedido.quantidade_dias,
                         data_inicio=dados_pedido.data_inicio,
                         data_devolucao=dados_pedido.data_devolucao,
                         alugada=dados_pedido.alugada,
                         pago=False)

    secao.add(novo_pedido)
    secao.flush()

    relacao_ferramenta_pedido = []

    for ferramenta in dados_pedido.ferramentas:
        relacao_ferramenta_pedido.append(Ferramentas_pedido(id_ferramenta=ferramenta.id_ferramenta,
                                                            id_pedido=novo_pedido.id,
                                                            quantidade=ferramenta.quantidade))
        
    secao.add_all(relacao_ferramenta_pedido)
    secao.flush()
    secao.commit()

    return {"id_pedido": novo_pedido.id, "chave_pix": CHAVE_PIX}





