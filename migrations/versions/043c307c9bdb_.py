"""empty message

Revision ID: 043c307c9bdb
Revises: 1b3159731477
Create Date: 2020-07-08 16:04:37.647185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '043c307c9bdb'
down_revision = '1b3159731477'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orders', 'courier_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orders', 'courier_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###