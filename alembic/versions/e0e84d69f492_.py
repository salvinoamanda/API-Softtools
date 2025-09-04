"""empty message

Revision ID: e0e84d69f492
Revises: 44ef747e9b53
Create Date: 2025-09-04 13:42:02.897196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from pathlib import Path
import sys
raiz_projeto = Path(__file__).resolve().parent.parent
sys.path.insert(0, raiz_projeto)
from src.myapp.security import get_password_hash


# revision identifiers, used by Alembic.
revision: str = 'e0e84d69f492'
down_revision: Union[str, Sequence[str], None] = '44ef747e9b53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    senha = "convidado"

    op.execute(f"INSERT INTO usuario (nome, email, senha, telefone, estado) VALUES ('convidado', 'convidado@email.com', '{get_password_hash(senha)}', '67999999999', 'fic')")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM usuario WHERE nome = 'convidado'")
