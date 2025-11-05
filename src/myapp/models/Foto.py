from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.myapp.database import Base
from src.myapp.models.Ferramenta import Ferramenta

class Foto(Base):
    __tablename__ = 'Foto'
    
    id: Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True, autoincrement=True)
    id_ferramenta: Mapped[int] = mapped_column(ForeignKey("ferramenta.id"), nullable=False)
    nome_arquivo: Mapped[str] = mapped_column(Text)

    ferramenta : Mapped[Ferramenta] = relationship('Ferramenta', backref='fotos')
    
