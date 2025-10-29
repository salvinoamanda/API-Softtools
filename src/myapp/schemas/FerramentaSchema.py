from pydantic import BaseModel, field_validator, model_validator
from decimal import Decimal
from typing import Optional, Annotated

class FerramentaSchema(BaseModel):
    id: int
    nome: str
    diaria: Decimal
    descricao: str
    status: str
    categoria: str
    chave_pix: str
    avaliacao: Decimal
    quantidade_avaliacoes: int
    id_proprietario: int
    quantidade_estoque: int

    @model_validator(mode="after")
    def format_enums(self):
        
        if str(self.categoria).isnumeric():
            if self.status == "0":
                self.status = 'DISPONIVEL'
            else:
                self.status = 'INDISPONIVEL'

        if str(self.categoria).isnumeric():
            map_categoria = {"0" : "MANUAL",
                            "1" : "ELETRICA",
                            "2" : "PNEUMATICA",
                            "3" : "HIDRAULICA",
                            "4" : "MEDICAO"
                            }
            
            self.categoria = map_categoria[self.categoria]

        return self
      
      

class FerramentaPreviewSchema(BaseModel):
    id: int
    nome: str
    diaria: Decimal
    categoria: str



class FerramentaCadastroSchema(BaseModel):
    nome: str
    diaria: Decimal
    descricao: str
    categoria: str
    chave_pix: str
    quantidade_estoque: int = 1

class FerramentaAtualizacaoSchema(BaseModel):
    id_ferramenta: int
    nome: Optional[str] = None
    diaria: Optional[Decimal] = None
    descricao: Optional[str] = None
    status: Optional[str] = None
    categoria: Optional[str] = None
    chave_pix: Optional[str] = None
    quantidade_estoque: Optional[int] = None

class AvaliacaoSchema(BaseModel):
    id_ferramenta: int
    avaliacao: Decimal

    @field_validator("avaliacao")
    def avaliacao_zero_a_cinca(cls, v):
        if v < 0 or v > 5:
            raise ValueError("Avaliação deve ser entre 0 e 5")
        
        return v
    
class FerramentaPedidoSchema(BaseModel):
    id_ferramenta: int
    quantidade: int