"""alter orders table

Revision ID: f588fe06ce4f
Revises: aa0044f1d417
Create Date: 2017-12-28 15:12:37.317536

"""
from alembic import op
import sqlalchemy as sa
import enum


# revision identifiers, used by Alembic.
revision = 'f588fe06ce4f'
down_revision = 'aa0044f1d417'
branch_labels = None
depends_on = None

metadata = sa.MetaData()

# payment_type = sa.Enum('cash', 'card', name='payment_type', metadata=metadata)


def upgrade():
    payment_type = sa.Enum('cash', 'card', name='payment_type', metadata=metadata)
    payment_type.create(op.get_bind())

    op.alter_column('orders', 'payment_type', type_=sa.Enum('cash', 'card', name='payment_type'),
                    postgresql_using='payment_type::payment_type')


def downgrade():
    pass
