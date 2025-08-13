from sqlalchemy.orm import Session
from sqlalchemy import select
from src.myapp.models.Ferramenta import Ferramenta
from src.myapp.models.Usuario import Usuario
from src.myapp.schemas.FerramentaSchema import FerramentaSchema

def readFerramentas(secao: Session, uf: str | None):

    

    if(uf is not None):
        statement = select(Ferramenta).join(Ferramenta.proprietario).where(Usuario.estado == uf)
    else:
        statement = select(Ferramenta)

    ferramentas = secao.scalars(statement).all()

    return list(map(lambda ferramenta: FerramentaSchema(
        id = ferramenta.id,
        nome = ferramenta.nome,
        diaria = ferramenta.diaria,
        descricao = ferramenta.descricao,
        status = ferramenta.status,
        categoria = ferramenta.categoria,
        chave_pix = ferramenta.chave_pix,
        avaliacao = ferramenta.avaliacao,
        quantidade_avaliacoes = ferramenta.quantidade_avaliacoes,
        id_proprietario = ferramenta.id_proprietario,
    ) , ferramentas))