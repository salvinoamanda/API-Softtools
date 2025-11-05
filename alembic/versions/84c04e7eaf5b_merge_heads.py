"""merge heads

Revision ID: 84c04e7eaf5b
Revises: 6e51b7adafe5, c1f9ad2db449
Create Date: 2025-11-04 20:03:33.958298

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84c04e7eaf5b'
down_revision: Union[str, Sequence[str], None] = ('6e51b7adafe5', 'c1f9ad2db449')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
