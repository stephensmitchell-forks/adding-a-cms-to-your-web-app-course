"""Add is shared to page

Revision ID: b2b441709daf
Revises: 72ddb1e97dfd
Create Date: 2020-06-07 09:01:30.421925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2b441709daf'
down_revision = '72ddb1e97dfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pages', sa.Column('is_shared', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pages', 'is_shared')
    # ### end Alembic commands ###