from pydantic import BaseModel
from src.myapp.schemas.FerramentaSchema import FerramentaPreviewSchema
from typing import List

class ItemCarrinhoSchema(BaseModel):
    ferramenta: FerramentaPreviewSchema

class CarrinhoSchema(BaseModel):
    ferramentas : List[ItemCarrinhoSchema]