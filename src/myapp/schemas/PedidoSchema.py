from pydantic import BaseModel
from datetime import datetime
from typing import List
from src.myapp.schemas.FerramentaSchema import FerramentaPedidoSchema

class PedidoSchema(BaseModel):

    ferramentas: List[FerramentaPedidoSchema]
    quantidade_dias: int
    data_inicio: datetime
    data_devolucao: datetime
    alugada: bool