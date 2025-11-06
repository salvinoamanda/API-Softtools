from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from fastapi import HTTPException, status, Depends
import os
from dotenv import load_dotenv

load_dotenv()

# Criação do engine com configurações seguras
engine = create_engine(
    os.getenv("DB_URL"),
    pool_size=10,          # número de conexões fixas
    max_overflow=20,       # conexões extras temporárias
    pool_timeout=30,       # tempo máximo para esperar uma conexão
    pool_recycle=1800,     # recicla conexões antigas a cada 30min
)

# Configura o factory das sessões
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Dependência para FastAPI (garante fechamento automático)
def get_session():
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao acessar o banco de dados: {e}"
        )
    finally:
        session.close()

# Base declarativa para os models
class Base(DeclarativeBase):
    pass
