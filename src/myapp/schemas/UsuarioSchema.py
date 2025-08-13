from pydantic import BaseModel, field_validator, BeforeValidator, EmailStr
from typing import Annotated, Optional

def isEmpty(value: str) -> str:
    if not value or not value.strip():
        raise ValueError("Campo obrigatório")
    
    return value
    

class UsuarioSchemaCadastro(BaseModel):
    nome: Annotated[str, BeforeValidator(isEmpty)]
    email: Annotated[EmailStr, BeforeValidator(isEmpty)]
    senha: Annotated[str, BeforeValidator(isEmpty)]
    telefone: Annotated[str, BeforeValidator(isEmpty)]
    estado: Annotated[str, BeforeValidator(isEmpty)]

    @field_validator("telefone", mode="before")
    def numerico(cls, v:str):
        if v.isnumeric():
            return v
        raise ValueError("Campo de telefone suporta apenas caracteres numéricos")


class UsuarioSchemaPublic(BaseModel):
    id: int
    nome: str
    email: EmailStr
    telefone: str
    estado: str
    
class UsuarioAutenticadoSchema(UsuarioSchemaPublic):
    access_token : str
    token_type: str


class UsuarioAtualizacaoSchema(BaseModel):
    id: int
    email: Annotated[Optional[str], BeforeValidator(isEmpty)] = None
    nome: Annotated[Optional[str], BeforeValidator(isEmpty)] = None
    telefone: Annotated[Optional[str], BeforeValidator(isEmpty)] = None
    senha: Annotated[Optional[str], BeforeValidator(isEmpty)] = None
    estado: Annotated[Optional[EmailStr], BeforeValidator(isEmpty)] = None

