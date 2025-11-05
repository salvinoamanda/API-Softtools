"""cria usuario convidado

Revision ID: b9cd537da8ed
Revises: 1ca1b7228cee
Create Date: 2025-11-04 20:58:42.480853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from src.myapp.security import get_password_hash


# revision identifiers, used by Alembic.
revision: str = 'b9cd537da8ed'
down_revision: Union[str, Sequence[str], None] = '1ca1b7228cee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

SENHA = 'convidado'

def upgrade() -> None:
    op.execute(f"INSERT INTO usuario (nome, email, senha, telefone, estado) VALUES ('convidado', 'convidado@email.com', '{get_password_hash(SENHA)}', '00000000000', 'MS');")
    


def downgrade() -> None:
    op.execute("DELETE FROM usuario WHERE nome = 'convidado'")    