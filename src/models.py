from sqlalchemy import Column, Integer, String
from src.database import Base


class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    quantidade_disponivel = Column(Integer, default=1)