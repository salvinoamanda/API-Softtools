from sqlalchemy import Integer, Date, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.myapp.database import Base

class Pedido(Base):

    __tablename__ = "pedido"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_solicitante = mapped_column(ForeignKey("usuario.id"))
    quantidade_dias : Mapped[int] = mapped_column(Integer, nullable=False)
    data_inicio: Mapped[datetime] = mapped_column(Date, nullable=False)
    data_devolucao: Mapped[datetime] = mapped_column(Date, nullable=False)
    alugada: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
