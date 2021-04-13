"""empty message

Revision ID: e7546eded155
Revises: 4b375f74d401
Create Date: 2021-04-08 23:16:56.303839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7546eded155'
down_revision = '4b375f74d401'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follower',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followee_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follower')
    # ### end Alembic commands ###