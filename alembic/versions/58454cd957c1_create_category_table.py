"""Create category table

Revision ID: 58454cd957c1
Revises: 1addff03b769
Create Date: 2017-12-14 15:01:32.010856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58454cd957c1'
down_revision = '1addff03b769'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'category',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cat_name', sa.String(100), unique=True),
        sa.Column('image', sa.String(20)),
        sa.Column('description', sa.Text),
        sa.Column('slug', sa.String(20), nullable=False),
        sa.Column('parent_id',sa.Integer, sa.ForeignKey('category.id')),
    )


def downgrade():
    op.drop_table('category')
