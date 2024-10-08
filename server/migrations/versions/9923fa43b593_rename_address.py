"""rename address

Revision ID: 9923fa43b593
Revises: 38b3e81c4b5b
Create Date: 2024-10-02 22:56:38.573640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9923fa43b593'
down_revision = '38b3e81c4b5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
