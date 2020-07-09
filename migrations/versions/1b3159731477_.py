"""empty message

Revision ID: 1b3159731477
Revises: 61f128f01eb1
Create Date: 2020-07-08 00:10:18.342934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b3159731477'
down_revision = '61f128f01eb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=180), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('couriers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=180), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=180), nullable=False),
    sa.Column('from_address', sa.String(), nullable=False),
    sa.Column('to_address', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('courier_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['courier_id'], ['couriers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.drop_table('orders')
    op.drop_table('couriers')
    op.drop_table('clients')
    # ### end Alembic commands ###