from sqlalchemy.orm import Session

from src.models import Emprestimo


class EmprestimoRepository:
    def criar(self, db: Session, emprestimo: Emprestimo):
        db.add(emprestimo)
        db.commit()
        db.refresh(emprestimo)
        return emprestimo

    def buscar_por_id(self, db: Session, emprestimo_id: int):
        return (
            db.query(Emprestimo)
            .filter(Emprestimo.id == emprestimo_id)
            .first()
        )
