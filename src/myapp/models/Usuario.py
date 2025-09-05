from src.myapp.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

class Usuario(Base):
    
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(200), nullable=False)
    telefone: Mapped[str] = mapped_column(String(15))
    estado : Mapped[str] = mapped_column(String(50), nullable=False)
    

