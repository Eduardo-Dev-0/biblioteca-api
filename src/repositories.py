from sqlalchemy.orm import Session

from src.models import Livro
from src.schemas import LivroCreate


class LivroRepository:
    def listar(self, db: Session):
        return db.query(Livro).all()

    def buscar_por_id(self, db: Session, livro_id: int):
        return db.query(Livro).filter(Livro.id == livro_id).first()

    def criar(self, db: Session, livro: LivroCreate):
        novo_livro = Livro(**livro.model_dump())
        db.add(novo_livro)
        db.commit()
        db.refresh(novo_livro)
        return novo_livro
