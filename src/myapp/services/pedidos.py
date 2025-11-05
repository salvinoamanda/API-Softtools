from sqlalchemy.orm import Session
from src.myapp.models.Pedido import Pedido
from src.myapp.models.Ferramentas_pedido import Ferramentas_pedido
from src.myapp.schemas.PedidoSchema import PedidoSchema
from src.myapp.models.Historico_aluguel import Historico_aluguel
from dotenv import load_dotenv
import os
from datetime import datetime

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
    relacao_historico = []

    for ferramenta in dados_pedido.ferramentas:
        relacao_ferramenta_pedido.append(Ferramentas_pedido(id_ferramenta=ferramenta.id_ferramenta,
                                                            id_pedido=novo_pedido.id,
                                                            quantidade=ferramenta.quantidade))
        
        relacao_historico.append(Historico_aluguel( id_cliente=id_usuario,
                                                    id_produto=ferramenta.id_ferramenta,
                                                    timestamp=datetime.now()))
        
    secao.add_all(relacao_ferramenta_pedido)
    secao.add_all(relacao_historico)
    secao.flush()
    secao.commit()

    return {"id_pedido": novo_pedido.id, "chave_pix": CHAVE_PIX}





