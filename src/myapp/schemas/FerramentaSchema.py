from pydantic import BaseModel, BeforeValidator
from decimal import Decimal
from typing import Optional, Annotated

'''id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
nome: Mapped[str] = mapped_column(String(100), nullable=False)
diaria: Mapped[Decimal] = mapped_column(DECIMAL(10,2), nullable = False)
descricao: Mapped[str] = mapped_column(Text, nullable = False)
status: Mapped[str] = mapped_column(sqlalchemy_enum(StatusFerramenta), nullable= False, default = StatusFerramenta.DISPONIVEL)
categoria: Mapped[str] = mapped_column(sqlalchemy_enum(CategoriaFerramenta), nullable=False)
chave_pix: Mapped[str] = mapped_column(Text, nullable=False)
avaliacao: Mapped[int] = mapped_column(Integer, default=0)
quantidade_avaliacoes: Mapped[int] = mapped_column(Integer, default = 0, nullable=True)
id_proprietario: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)'''

class FerramentaSchema(BaseModel):
    id: int
    nome: str
    diaria: Decimal
    descricao: str
    status: str
    categoria: str
    chave_pix: str
    avaliacao: int
    quantidade_avaliacoes: int
    id_proprietario: int
    quantidade_estoque: int


class FerramentaPreviewSchema(BaseModel):
    id: int
    nome: str
    diaria: Decimal
    categoria: str



class FerramentaCadastroSchema(BaseModel):
    nome: str
    diaria: Decimal
    descricao: str
    categoria: str
    chave_pix: str
    quantidade_estoque: int = 1