"""Add is_pinned column to log_post table

Revision ID: ecd90d2ecd32
Revises: 179c22e19a6f
Create Date: 2021-10-21 04:10:48.396149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecd90d2ecd32'
down_revision = '179c22e19a6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('log_post', sa.Column('is_pinned', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('log_post', 'is_pinned')
    # ### end Alembic commands ###