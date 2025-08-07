from src.myapp.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from src.myapp.models.Ferramenta import Ferramenta
from typing import List
from src.myapp.models.Historico_aluguel import Historico_aluguel

class Usuario(Base):
    
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(200), nullable=False)
    telefone: Mapped[str] = mapped_column(String(15))

    ferramentas: Mapped[list[Ferramenta]] = relationship(back_populates="propietario_ferramentas")
    
    historicoAlugueis: Mapped[List[Historico_aluguel]] = relationship(back_populates="locatario")

    

