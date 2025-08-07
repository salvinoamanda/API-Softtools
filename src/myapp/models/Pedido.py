from sqlalchemy import Integer, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List
from src.myapp.models.Ferramentas_pedido import Ferramentas_pedido

class Pedido:

    __tablename__ = "pedido"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantidade_dias : Mapped[int] = mapped_column(Integer, nullable=False)
    data_inicio: Mapped[datetime] = mapped_column(Date, nullable=False)
    data_devolucao: Mapped[datetime] = mapped_column(Date, nullable=False)
    alugada: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    ferramentas: Mapped[List[Ferramentas_pedido]] = relationship(back_populates="pedido")