from fastapi import APIRouter, status, Depends
from src.myapp.schemas.UsuarioSchema import UsuarioSchemaCadastro, UsuarioAutenticadoSchema, UsuarioSchemaPublic, UsuarioAtualizacaoSchema
from src.myapp.services.usuarios import createUsuario, autenticacao, atualizarUsuario
from http import HTTPStatus
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.myapp.database import get_session
from src.myapp.security import auth_validation

usuarios_router = APIRouter(prefix='/users')

#Cadastro de usuários
@usuarios_router.post("/", status_code= status.HTTP_201_CREATED)
async def cadastro (dadosCadastro: UsuarioSchemaCadastro, secao: Session = Depends(get_session), _: str = Depends(auth_validation)):
    createUsuario(dadosCadastro, secao)
    return dadosCadastro


#Login de usuários
@usuarios_router.post("/auth", status_code=status.HTTP_202_ACCEPTED, response_model = UsuarioAutenticadoSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), secao: Session = Depends(get_session)):
    
    return autenticacao(email=form_data.username, senha=form_data.password, session=secao)

#Atualiza usuários
@usuarios_router.put("/", status_code=HTTPStatus.OK, response_model=UsuarioSchemaPublic)
async def put_usuarios(request : UsuarioAtualizacaoSchema, 
                       secao: Session = Depends(get_session), 
                       _: str = Depends(auth_validation)):
    
    return atualizarUsuario(request, secao)
