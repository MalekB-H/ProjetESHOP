"""add content in posts

Revision ID: 6188101b7171
Revises: 92a555909925
Create Date: 2023-05-02 15:15:17.009528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6188101b7171'
down_revision = '92a555909925'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
