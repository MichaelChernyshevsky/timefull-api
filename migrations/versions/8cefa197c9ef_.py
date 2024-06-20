"""empty message

Revision ID: 8cefa197c9ef
Revises: a23581e3e342
Create Date: 2024-06-20 17:31:07.647405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cefa197c9ef'
down_revision = 'a23581e3e342'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=250),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.String(length=250),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
