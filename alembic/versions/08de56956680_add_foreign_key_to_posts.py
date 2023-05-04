"""add foreign-key to posts

Revision ID: 08de56956680
Revises: cf84250af4a3
Create Date: 2023-05-02 15:28:38.630928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08de56956680'
down_revision = 'cf84250af4a3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts',"user_id")
    pass
