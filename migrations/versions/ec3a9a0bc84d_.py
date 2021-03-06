"""empty message

Revision ID: ec3a9a0bc84d
Revises: e2d96a224173
Create Date: 2019-04-07 08:10:50.032722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec3a9a0bc84d'
down_revision = 'e2d96a224173'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('balance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('secure_token', sa.String(length=128), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_balance_secure_token'), 'balance', ['secure_token'], unique=False)
    op.create_table('billing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('secure_token', sa.String(length=128), nullable=True),
    sa.Column('address_1', sa.Text(), nullable=True),
    sa.Column('address_2', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_billing_secure_token'), 'billing', ['secure_token'], unique=False)
    op.create_table('meters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('secure_token', sa.String(length=128), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_meters_secure_token'), 'meters', ['secure_token'], unique=False)
    op.create_table('sensors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('meter_id', sa.Integer(), nullable=True),
    sa.Column('secure_token', sa.String(length=128), nullable=True),
    sa.Column('sensor_type', sa.String(length=128), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['meter_id'], ['meters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensors_secure_token'), 'sensors', ['secure_token'], unique=False)
    op.create_index(op.f('ix_sensors_sensor_type'), 'sensors', ['sensor_type'], unique=False)
    op.create_table('readings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('meter_id', sa.Integer(), nullable=True),
    sa.Column('secure_token', sa.String(length=128), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['meter_id'], ['sensors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_readings_secure_token'), 'readings', ['secure_token'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_readings_secure_token'), table_name='readings')
    op.drop_table('readings')
    op.drop_index(op.f('ix_sensors_sensor_type'), table_name='sensors')
    op.drop_index(op.f('ix_sensors_secure_token'), table_name='sensors')
    op.drop_table('sensors')
    op.drop_index(op.f('ix_meters_secure_token'), table_name='meters')
    op.drop_table('meters')
    op.drop_index(op.f('ix_billing_secure_token'), table_name='billing')
    op.drop_table('billing')
    op.drop_index(op.f('ix_balance_secure_token'), table_name='balance')
    op.drop_table('balance')
    # ### end Alembic commands ###
