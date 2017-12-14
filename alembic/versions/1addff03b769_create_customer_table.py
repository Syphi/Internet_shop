"""Create customer table

Revision ID: 1addff03b769
Revises: 
Create Date: 2017-12-14 14:54:53.165216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1addff03b769'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customer',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_name', sa.String(25), nullable=False),
        sa.Column('email', sa.String(25), unique=True),
        sa.Column('password', sa.String(15), nullable=False),
        sa.Column('phone', sa.String(10)),
        sa.Column('shipping_address', sa.Text),
    )


def downgrade():
    op.drop_table('customer')
