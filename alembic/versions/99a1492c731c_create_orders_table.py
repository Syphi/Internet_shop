"""Create orders table

Revision ID: 99a1492c731c
Revises: cbb21ec22746
Create Date: 2017-12-14 15:01:58.445832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a1492c731c'
down_revision = 'cbb21ec22746'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('customer_id',sa.Integer, sa.ForeignKey('customer.id')),
        sa.Column('sum_price', sa.Numeric, nullable=False),
        sa.Column('delivery_data_time', sa.TIMESTAMP),
        sa.Column('payment_type', sa.String(4), sa.CheckConstraint('payment_type' in ('cash', 'card'))),
    )


def downgrade():
    op.drop_table('orders')
