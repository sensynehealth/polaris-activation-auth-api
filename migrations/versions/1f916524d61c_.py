"""empty message

Revision ID: 1f916524d61c
Revises: ba93cab856a0
Create Date: 2018-03-08 18:35:11.595492

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1f916524d61c"
down_revision = "ba93cab856a0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user", sa.Column("authorisation_code_salt", sa.String(), nullable=True)
    )
    op.add_column(
        "user", sa.Column("hashed_authorisation_code", sa.LargeBinary(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "hashed_authorisation_code")
    op.drop_column("user", "authorisation_code_salt")
    # ### end Alembic commands ###
