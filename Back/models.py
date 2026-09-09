from Back.dependencies.database import Base
from sqlalchemy import (
    String,
    DateTime,
    Enum as SQLEnum,
    Date,
    func,
    CheckConstraint,
    UniqueConstraint,
    ForeignKey,
)
from datetime import datetime, date
from sqlalchemy.orm import Mapped, mapped_column
from enums import AcessoTipos, MovimentacoesTipos


class Marcas(Base):
    __tablename__ = "marcas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)


class Usuarios(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)
    nome: Mapped[str] = mapped_column(String(255), nullable=False)
    sobrenome: Mapped[str] = mapped_column(String(255), nullable=False)
    contato: Mapped[str] = mapped_column(String(255), nullable=False)
    acesso: Mapped[AcessoTipos] = mapped_column(
        SQLEnum(AcessoTipos, name="acesso_tipos"), nullable=False
    )
    data_nascimento: Mapped[Date] = mapped_column(Date, nullable=False)


class Produtos(Base):
    __tablename__ = "produtos"
    id: Mapped[int] = mapped_column(primary_key=True)
    marca_id: Mapped[int] = mapped_column(ForeignKey("marca.id"), nullable=False)
    produto_nome: Mapped[str] = mapped_column(String(255), nullable=False)
    produto_descricao: Mapped[str] = mapped_column(String(255), nullable=False)
    quantidade_minima_unidades: Mapped[int] = mapped_column(nullable=False)
    produto_codigo_barras: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True
    )


class Lotes(Base):
    __tablename__ = "lotes"
    __table_args__ = (
        CheckConstraint("lote_quantidade_atual >= 0", name="ck_lote_quantidade_atual"),
        CheckConstraint(
            "lote_data_vencimento > lote_data_fabricacao", name="ck_lote_datas"
        ),
        UniqueConstraint("produto_id", "lote_numero", name="uq_produto_lote"),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    produto_id: Mapped[int] = mapped_column(ForeignKey("produto.id"), nullable=False)
    lote_quantidade_atual: Mapped[int] = mapped_column(nullable=False)
    lote_numero: Mapped[str] = mapped_column(String(50), nullable=False)
    lote_data_registro: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    lote_data_vencimento: Mapped[date] = mapped_column(Date, nullable=False)
    lote_data_fabricacao: Mapped[date] = mapped_column(Date, nullable=False)


class MovimentacoesEstoque(Base):
    __tablename__ = "movimentacoes_estoque"
    __table_args__ = (CheckConstraint("quantidade_unidades > 0", name="ck_quantidade_unidades"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    lote_id: Mapped[int] = mapped_column(ForeignKey("lotes.id"), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    movimentacoes_estoque_tipo: Mapped[MovimentacoesTipos] = mapped_column(
        SQLEnum(MovimentacoesTipos, name="movimentacoes_tipos"), nullable=False
    )
    quantidade_unidade: Mapped[int] = mapped_column(nullable=False)
    movimentacoes_estoque_motivo: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    movimentacoes_estoque_data: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
