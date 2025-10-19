from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from src.myapp.models.Usuario import Usuario
from src.myapp.schemas.UsuarioSchema import (
    UsuarioSchemaPublic,
    UsuarioSchemaCadastro,
    UsuarioAutenticadoSchema,
    UsuarioAtualizacaoSchema,
)
from fastapi import HTTPException, status
from http import HTTPStatus
from src.myapp.security import get_password_hash, verify_password, create_access_token


def buscaUsuarioPorID(id: int, secao: Session) -> Usuario | None:
    try:
        usuario = secao.scalar(select(Usuario).where(Usuario.id == id))
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado"
            )
        return usuario
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Falha ao consultar o banco de dados.",
        )


def createUsuario(cadastro: UsuarioSchemaCadastro, secao: Session):
    statement = select(Usuario).where(Usuario.email == cadastro.email)

    db_usuario = secao.scalar(statement)

    if db_usuario:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail="Email já cadastrado"
        )

    # Cria o hash da senha
    hash_senha = get_password_hash(cadastro.senha)

    db_usuario = Usuario(
        nome=cadastro.nome,
        email=cadastro.email,
        senha=hash_senha,
        telefone=cadastro.telefone,
        estado=cadastro.estado,
    )

    secao.add(db_usuario)
    secao.commit()
    secao.refresh(db_usuario)


def autenticacao(email: str, senha: str, session: Session):
    user = session.scalar(select(Usuario).where(Usuario.email == email))

    if not user or not verify_password(senha, user.senha):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail="Email ou senha inválidos"
        )

    data = {"email": email, "id": user.id}

    token = create_access_token(data)

    return UsuarioAutenticadoSchema(
        id=user.id,
        email=user.email,
        nome=user.nome,
        telefone=user.telefone,
        estado=user.estado,
        access_token=token,
        token_type="Bearer",
    )


def atualizarUsuario(dados: UsuarioAtualizacaoSchema, secao: Session) -> Usuario:
    usuario = buscaUsuarioPorID(dados.id, secao)

    if dados.email is not None:
        statement = select(Usuario).where(
            and_(Usuario.email == dados.email, Usuario.id != dados.id)
        )

        if secao.scalar(statement):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="Email já cadastrado"
            )

        usuario.email = dados.email

    if dados.nome is not None:
        usuario.nome = dados.nome

    if dados.telefone is not None:
        usuario.telefone = dados.telefone

    if dados.senha is not None:
        hash_senha = get_password_hash(dados.senha)
        usuario.senha = hash_senha

    secao.commit()

    secao.refresh(usuario)

    return UsuarioSchemaPublic(
        id=usuario.id,
        email=usuario.email,
        nome=usuario.nome,
        telefone=usuario.telefone,
        estado=usuario.estado,
    )


# Função para excluir usuário pode ser adicionada aqui no futuro
def excluirUsuario(id: int, secao: Session):
    usuario = buscaUsuarioPorID(id, secao)

    secao.delete(usuario)
    secao.commit()


# Retorna todos os usuários
def getAllUsuarios(secao: Session) -> list[UsuarioSchemaPublic]:
    usuarios = secao.scalars(select(Usuario)).all()

    return [
        UsuarioSchemaPublic(
            id=u.id, email=u.email, nome=u.nome, telefone=u.telefone, estado=u.estado
        )
        for u in usuarios
    ]
