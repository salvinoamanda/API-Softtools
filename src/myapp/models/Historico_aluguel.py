

from src.myapp.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, TIMESTAMP, ForeignKey
from datetime import datetime, timezone
from src.myapp.models.Usuario import Usuario
from src.myapp.models.Ferramenta import Ferramenta


class Historico_aluguel(Base):
    
    __tablename__ = "historico_aluguel"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_cliente : Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    id_produto: Mapped[int] = mapped_column(ForeignKey("ferramenta.id"), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    
    locatario : Mapped[Usuario] = relationship(back_populates="historicoAlugueis")
    produtoAlugado: Mapped[Ferramenta] = relationship(back_populates="historicoAlugado")