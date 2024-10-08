"""empty message

Revision ID: 3abd8ede7006
Revises: 1d5fff2c57bc
Create Date: 2024-09-30 18:43:42.624718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3abd8ede7006'
down_revision = '1d5fff2c57bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.alter_column('category_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.create_foreign_key(batch_op.f('fk_workouts_category_id_categories'), 'categories', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_workouts_category_id_categories'), type_='foreignkey')
        batch_op.alter_column('category_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    # ### end Alembic commands ###
