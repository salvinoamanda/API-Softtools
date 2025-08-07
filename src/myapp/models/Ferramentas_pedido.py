'''CREATE TABLE Ferramentas_pedido (Id_pedi INTEGER,
								 Id_ferramentas SERIAL,
								 Id_prod INTEGER,
								 
								 PRIMARY KEY (Id_pedi, Id_ferramentas),
								 FOREIGN KEY (Id_pedi) REFERENCES Pedido(Id_pedido),
								 FOREIGN KEY (Id_prod) REFERENCES Ferramenta(Id_produto));'''

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.myapp.models.Ferramenta import Ferramenta
from src.myapp.models.Pedido import Pedido

class Ferramentas_pedido:

    __tablename__ = "ferramentas_pedido"

    id_ferramenta: Mapped[int] = mapped_column(ForeignKey("ferramenta.id"), primary_key=True)
    id_pedido: Mapped[int] = mapped_column(ForeignKey("pedido"), primary_key=True)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    
    ferramenta: Mapped[Ferramenta] = relationship(back_populates="pedidos")
    pedido: Mapped[Pedido] = relationship(back_populates="ferramentas")
