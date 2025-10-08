from src.myapp.models.Ferramenta import Ferramenta
from sqlalchemy.orm import Session
from src.myapp.schemas.FerramentaSchema import FerramentaSchema

def historico_registro(id_usuario: int, sessao: Session):
    historico = []
    
    ferramentas = sessao.query(Ferramenta).filter(id_usuario == Ferramenta.id_proprietario)
    
    for ferramenta in ferramentas:
        historico.append(FerramentaSchema(id=ferramenta.id, nome=ferramenta.nome, diaria=ferramenta.diaria, status=ferramenta.status, categoria=ferramenta.categoria, chave_pix=ferramenta.chave_pix, avaliacao=ferramenta.avaliacao, quantidade_avaliacoes=ferramenta.quantidade_avaliacoes, id_proprietario=ferramenta.id_proprietario, descricao=ferramenta.descricao, quantidade_estoque=ferramenta.quantidade_estoque))

    return historico





