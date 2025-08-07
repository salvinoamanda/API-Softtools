'''CREATE TABLE Carrinho (Id_cliente INTEGER,
					   Id_pedi INTEGER,
					   
					   PRIMARY KEY (Id_cliente, Id_pedi),
					   FOREIGN KEY (Id_cliente) REFERENCES Usuario(Id_usuario),
					   FOREIGN KEY (Id_pedi) REFERENCES Pedido(Id_pedido));'''

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

class Carrinho:
    id_cliente: Mapped[int] = mapped_column(ForeignKey("usuario.id"), primary_key=True)
    id_pedido: Mapped[int] = mapped_column(ForeignKey("pedido.id"), primary_key=True)
	

	