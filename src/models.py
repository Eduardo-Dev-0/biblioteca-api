from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from src.database import Base


class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    quantidade_disponivel = Column(Integer, default=1)


class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True, index=True)
    livro_id = Column(Integer, ForeignKey("livros.id"), nullable=False)
    leitor = Column(String, nullable=False)
    data_emprestimo = Column(DateTime, default=datetime.now)
