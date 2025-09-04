from src.myapp.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import List
from src.myapp.models.Pedido import Pedido
from src.myapp.models.ItemCarrinho import ItemCarrinho

class Usuario(Base):
    
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(200), nullable=False)
    telefone: Mapped[str] = mapped_column(String(15))
    estado : Mapped[str] = mapped_column(String(50), nullable=False)
    
    carrinho_items: Mapped[List[ItemCarrinho]] = relationship(
    back_populates="usuario",
    cascade="all, delete-orphan",
    )


