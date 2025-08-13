from src.myapp.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import List
from src.myapp.models.Pedido import Pedido
from src.myapp.models.Carrinho import carrinho

class Usuario(Base):
    
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(200), nullable=False)
    telefone: Mapped[str] = mapped_column(String(15))
    estado : Mapped[str] = mapped_column(String(50), nullable=False)
    
    carrinho: Mapped[List[Pedido]] = relationship('Pedido', secondary=carrinho, backref='usuario_alugou')


