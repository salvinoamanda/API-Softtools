from pydantic import BaseModel
from src.myapp.schemas.FerramentaSchema import FerramentaPreviewSchema
from typing import List
from decimal import Decimal

class ItemCarrinhoSchema(BaseModel):
    ferramenta: FerramentaPreviewSchema
    quantidade: int
    valorTotalDiaria: Decimal

class CarrinhoSchema(BaseModel):
    ferramentas : List[ItemCarrinhoSchema]
    valorTotalPreliminar: Decimal