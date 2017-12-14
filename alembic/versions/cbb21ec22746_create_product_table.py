"""Create product table

Revision ID: cbb21ec22746
Revises: 58454cd957c1
Create Date: 2017-12-14 15:01:48.468996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbb21ec22746'
down_revision = '58454cd957c1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('category.id')),
        sa.Column('prod_name', sa.String(15), unique=True),
        sa.Column('image', sa.String(20)),
        sa.Column('description', sa.Text),
        sa.Column('slug', sa.String(20), unique=True),
        sa.Column('price_ua', sa.Numeric, nullable=False),
        sa.Column('in_stock', sa.SmallInteger, nullable=False),
        sa.Column('other_info', sa.JSON)
    )


def downgrade():
    op.drop_table('product')
