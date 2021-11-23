"""Migrate Data

Revision ID: ecd6c0baff36
Revises: ac3ddad49c59
Create Date: 2021-11-22 20:17:00.054028

"""
from alembic import op
import sqlalchemy as sa

from data_extractor.functions import migrate

# revision identifiers, used by Alembic.
revision = 'ecd6c0baff36'
down_revision = 'ac3ddad49c59'
branch_labels = None
depends_on = None


def upgrade():
    migrate()


def downgrade():
    op.execute("TRUNCATE category CASCADE")
    op.execute("TRUNCATE food CASCADE")
    op.execute("TRUNCATE nutrient CASCADE")
    op.execute("TRUNCATE foodnutrient CASCADE")
