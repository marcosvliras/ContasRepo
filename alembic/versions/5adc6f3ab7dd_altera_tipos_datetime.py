"""altera tipos datetime

Revision ID: 5adc6f3ab7dd
Revises: 
Create Date: 2023-06-22 14:13:26.040260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5adc6f3ab7dd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "fornecedor_cliente",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "contas_a_pagar_e_receber",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("description", sa.String(length=36), nullable=True),
        sa.Column("valor", sa.Numeric(), nullable=True),
        sa.Column("tipo", sa.String(length=30), nullable=True),
        sa.Column("data_previsao", sa.Date(), nullable=True),
        sa.Column("data_baixa", sa.DateTime(), nullable=True),
        sa.Column("valor_baixa", sa.Numeric(), nullable=True),
        sa.Column("esta_baixada", sa.Boolean(), nullable=True),
        sa.Column("fornecedor_cliente_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["fornecedor_cliente_id"],
            ["fornecedor_cliente.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("contas_a_pagar_e_receber")
    op.drop_table("fornecedor_cliente")
    # ### end Alembic commands ###