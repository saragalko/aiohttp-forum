"""create table Message

Revision ID: 8ee45336f4d9
Revises: 
Create Date: 2024-04-29 21:12:02.130649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ee45336f4d9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    # ### end Alembic commands ###
