"""Create orders_product table

Revision ID: aa0044f1d417
Revises: 99a1492c731c
Create Date: 2017-12-14 15:02:16.095848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa0044f1d417'
down_revision = '99a1492c731c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'order_products',
        sa.Column('orders_id',sa.Integer, sa.ForeignKey('orders.id')),
        sa.Column('product_id',sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('number_prod', sa.Integer),
    )


def downgrade():
    op.drop_table('order_products')
