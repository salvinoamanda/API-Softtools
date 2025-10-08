from pydantic import BaseModel
from src.myapp.schemas.FerramentaSchema import FerramentaPreviewSchema
from datetime import datetime

class ItemHistoricoSchema(BaseModel):
    timestamp: datetime
    produto: FerramentaPreviewSchema