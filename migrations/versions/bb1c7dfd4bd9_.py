"""empty message

Revision ID: bb1c7dfd4bd9
Revises: bd0545e5ea29
Create Date: 2022-04-24 13:43:43.427646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb1c7dfd4bd9'
down_revision = 'bd0545e5ea29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usage-stamps', sa.Column('time_stamp', sa.DateTime(), nullable=False))
    op.add_column('usage-stamps', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False))
    op.create_index(op.f('ix_usage-stamps_time_stamp'), 'usage-stamps', ['time_stamp'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_usage-stamps_time_stamp'), table_name='usage-stamps')
    op.drop_column('usage-stamps', 'updated_at')
    op.drop_column('usage-stamps', 'time_stamp')
    # ### end Alembic commands ###