"""empty message

Revision ID: 8eb7d569652e
Revises: 6bb9e6ab6628
Create Date: 2018-11-08 10:41:51.857005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8eb7d569652e'
down_revision = '6bb9e6ab6628'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('busca',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('usuario', sa.Integer(), nullable=True),
    sa.Column('busca', sa.String(), nullable=True),
    sa.Column('buscado_em', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('busca')
    # ### end Alembic commands ###