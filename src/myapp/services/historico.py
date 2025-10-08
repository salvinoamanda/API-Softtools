from sqlalchemy.orm import Session
from src.myapp.models.Historico_aluguel import Historico_aluguel
from src.myapp.schemas.HistoricoSchema import ItemHistoricoSchema
from src.myapp.models.Ferramenta import Ferramenta
from src.myapp.schemas.FerramentaSchema import FerramentaPreviewSchema
from typing import List

def ferramenta_model_to_schema(model: Ferramenta) -> FerramentaPreviewSchema:
    return FerramentaPreviewSchema(id=model.id, diaria=model.diaria, categoria=model.categoria, nome=model.nome)


def readHistoricoAlugueis(idUsuario: int, secao: Session) -> List[ItemHistoricoSchema]:
    historico = secao.query(Historico_aluguel).where(Historico_aluguel.id_cliente == idUsuario)

    return map(lambda item: 
               ItemHistoricoSchema(timestamp=item.timestamp, 
                                                produto=ferramenta_model_to_schema(item.produto)),
                                                historico)

    
    

