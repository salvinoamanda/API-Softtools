'''CREATE TABLE Historico_aluguel (Id_cliente INTEGER,
								Id_prod INTEGER,
								
								PRIMARY KEY (Id_cliente, Id_prod),
								FOREIGN KEY (Id_cliente) REFERENCES Usuario(Id_usuario),
								FOREIGN KEY (Id_prod) REFERENCES Ferramenta(Id_produto));'''

from src.myapp.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, TIMESTAMP
from datetime import datetime, timezone


class Historico_aluguel(Base):
    id_cliente : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_produto: Mapped[int] = mapped_column(Integer, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))

    


