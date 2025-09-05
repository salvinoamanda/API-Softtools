from src.myapp.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Text, DECIMAL, Enum as sqlalchemy_enum, ForeignKey, text
from decimal import Decimal
from enum import Enum
from src.myapp.models.Usuario import Usuario

class StatusFerramenta(Enum):
    DISPONIVEL = 0
    ALUGADA = 1
    
class CategoriaFerramenta(Enum):
    MANUAL = 0
    ELETRICA = 1
    PNEUMATICA = 2
    HIDRAULICA = 3
    MEDICAO = 4

class Ferramenta(Base):
    __tablename__ = "ferramenta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    diaria: Mapped[Decimal] = mapped_column(DECIMAL(10,2), nullable = False)
    descricao: Mapped[str] = mapped_column(Text, nullable = False)
    status: Mapped[str] = mapped_column(sqlalchemy_enum(StatusFerramenta), nullable= False, default = StatusFerramenta.DISPONIVEL)
    categoria: Mapped[str] = mapped_column(sqlalchemy_enum(CategoriaFerramenta), nullable=False)
    chave_pix: Mapped[str] = mapped_column(Text, nullable=False)
    avaliacao: Mapped[int] = mapped_column(Integer, default=0)
    quantidade_avaliacoes: Mapped[int] = mapped_column(Integer, default = 0, nullable=True)
    id_proprietario: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    quantidade_estoque: Mapped[int] = mapped_column(Integer, default=1)


    proprietario : Mapped[Usuario] = relationship('Usuario', backref='ferramentas')