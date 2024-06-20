"""empty message

Revision ID: 76d502993c82
Revises: e066e90eb900
Create Date: 2024-06-20 17:02:09.696265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76d502993c82'
down_revision = 'e066e90eb900'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('economy',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=250), nullable=True),
    sa.Column('income', sa.Boolean(), nullable=True),
    sa.Column('count', sa.String(length=1000), nullable=True),
    sa.Column('date', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('economy')
    # ### end Alembic commands ###
