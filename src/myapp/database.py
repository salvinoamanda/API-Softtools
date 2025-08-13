from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os
from dotenv import load_dotenv
from fastapi import HTTPException, status

load_dotenv()
engine = create_engine(os.getenv("DB_URL"))

def get_session():
    try:
        Session = sessionmaker(bind=engine)
        return Session()
    except:
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                      detail="Erro ao conectar com o banco de dados")
        
class Base(DeclarativeBase):
    pass