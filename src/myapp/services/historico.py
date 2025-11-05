from sqlalchemy.orm import Session
from src.myapp.models.Historico_aluguel import Historico_aluguel
from src.myapp.schemas.HistoricoSchema import ItemHistoricoSchema
from src.myapp.models.Ferramenta import Ferramenta
from src.myapp.schemas.FerramentaSchema import FerramentaPreviewSchema, FerramentaSchema
from typing import List
from src.myapp.models.Foto import Foto

def ferramenta_model_to_schema(model: Ferramenta, ids_fotos: List[int]) -> FerramentaPreviewSchema:
    return FerramentaPreviewSchema(id=model.id, 
                                   diaria=model.diaria, 
                                   categoria=model.categoria, 
                                   nome=model.nome,
                                   ids_foto=ids_fotos)


def readHistoricoAlugueis(idUsuario: int, secao: Session) -> List[ItemHistoricoSchema]:
    historico = secao.query(Historico_aluguel).where(Historico_aluguel.id_cliente == idUsuario)

    schemas = []

    for item in historico:
        fotos = secao.query(Foto).where(Foto.id_ferramenta == item.id_produto)
        
        schemas.append(ItemHistoricoSchema(timestamp=item.timestamp, 
                                            produto=ferramenta_model_to_schema(item.produto, [f.id for f in fotos])))

    return schemas
               

def historico_registro(id_usuario: int, sessao: Session):
    historico = []
    
    ferramentas = sessao.query(Ferramenta).filter(id_usuario == Ferramenta.id_proprietario)
    
    for ferramenta in ferramentas:
        fotos = sessao.query(Foto).where(Foto.id_ferramenta == ferramenta.id)

        ids_fotos = [f.id for f in fotos]

        historico.append(FerramentaPreviewSchema(id=ferramenta.id, 
                                diaria=ferramenta.diaria, 
                                categoria=ferramenta.categoria, 
                                nome=ferramenta.nome,
                                ids_foto=ids_fotos))


    return historico

    
    

