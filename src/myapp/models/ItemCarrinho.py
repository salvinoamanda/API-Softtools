from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.myapp.database import Base


class ItemCarrinho(Base):
    __tablename__ = "item_carrinho"

    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False, primary_key=True)
    id_ferramenta: Mapped[int] = mapped_column(ForeignKey("ferramenta.id"), nullable=False, primary_key=True)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    ferramenta: Mapped["Ferramenta"] = relationship( "Ferramenta",
        foreign_keys=[id_ferramenta],
        uselist=False )