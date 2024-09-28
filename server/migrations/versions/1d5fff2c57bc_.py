"""empty message

Revision ID: 1d5fff2c57bc
Revises: 
Create Date: 2024-09-26 18:41:43.638529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d5fff2c57bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('category_id', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('videourl', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('programs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_programs_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('program_workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('program_id', sa.Integer(), nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.Column('sets', sa.Integer(), nullable=False),
    sa.Column('reps', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['program_id'], ['programs.id'], name=op.f('fk_program_workouts_program_id_programs')),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], name=op.f('fk_program_workouts_workout_id_workouts')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('program_workouts')
    op.drop_table('programs')
    op.drop_table('workouts')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
