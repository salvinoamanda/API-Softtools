"""empty message

Revision ID: c1f9ad2db449
Revises: edccd19fbc0b
Create Date: 2025-09-18 13:36:58.056816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1f9ad2db449'
down_revision: Union[str, Sequence[str], None] = 'edccd19fbc0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('ferramenta', 'status', existing_type=enumerate(["DISPONIVEL", "ALUGADA", "EXCLUIDA"]))


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('ferramenta', 'status', existing_type=enumerate(["DISPONIVEL", "ALUGADA"]))

