from fastapi import APIRouter, status, Depends
from src.myapp.schemas.UsuarioSchema import UsuarioSchemaCadastro, UsuarioAutenticadoSchema, UsuarioSchemaPublic, UsuarioAtualizacaoSchema
from src.myapp.services.usuarios import createUsuario, autenticacao, atualizarUsuario, getUsuario
from http import HTTPStatus
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.myapp.database import get_session
from src.myapp.security import auth_validation
from src.myapp.services.usuarios import excluirUsuario
from src.myapp.services.usuarios import getAllUsuarios

usuarios_router = APIRouter(prefix='/users')

#Cadastro de usuários
@usuarios_router.post("/", status_code= status.HTTP_201_CREATED)
async def cadastro (dadosCadastro: UsuarioSchemaCadastro, secao: Session = Depends(get_session)):
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

# Excluir usuários
@usuarios_router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuarios(idUsuario: int,
                          secao: Session = Depends(get_session),
                          _: str = Depends(auth_validation)):
    
    # Lógica para excluir o usuário
    excluirUsuario(idUsuario, secao)
    return None

# Lista usuários do sistema
@usuarios_router.get("/", response_model=list[UsuarioSchemaPublic], status_code=status.HTTP_200_OK)
async def get_usuarios(secao: Session = Depends(get_session), _: str = Depends(auth_validation)):
    return getAllUsuarios(secao)


@usuarios_router.get("/{id_usuario}", response_model=UsuarioSchemaPublic, status_code=status.HTTP_200_OK)
async def get_usuario(id_usuario: int, 
                       secao: Session = Depends(get_session), 
                       _: str = Depends(auth_validation)):
    return getUsuario(id_usuario, secao)




