"""empty message

Revision ID: 15bc4aa0d87f
Revises: 63bb88f43ac1
Create Date: 2024-06-13 13:50:27.438733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15bc4aa0d87f'
down_revision = '63bb88f43ac1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=True),
    sa.Column('phone', sa.String(length=250), nullable=True),
    sa.Column('sex', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
