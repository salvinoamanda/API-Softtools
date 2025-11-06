from src.myapp.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DECIMAL
from decimal import Decimal


class Avaliacao_usuario_ferramenta(Base):
    
    __tablename__ = "avaliacao_usuario_ferramenta"

    id_cliente : Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False, primary_key=True)
    id_produto: Mapped[int] = mapped_column(ForeignKey("ferramenta.id"), nullable=False, primary_key=True)
    avaliacao: Mapped[Decimal] = mapped_column(DECIMAL(10,2), default=0)
