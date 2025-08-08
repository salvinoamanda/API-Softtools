'''CREATE TABLE Carrinho (Id_cliente INTEGER,
					   Id_pedi INTEGER,
					   
					   PRIMARY KEY (Id_cliente, Id_pedi),
					   FOREIGN KEY (Id_cliente) REFERENCES Usuario(Id_usuario),
					   FOREIGN KEY (Id_pedi) REFERENCES Pedido(Id_pedido));'''

from sqlalchemy import ForeignKey, Integer, Table, Column
from src.myapp.database import Base


	
carrinho = Table('carrinho', 
                 Base.metadata,
                 Column('id_cliente', Integer, ForeignKey("usuario.id"), primary_key=True),
                 Column('id_pedido', Integer, ForeignKey("pedido.id"), primary_key=True))