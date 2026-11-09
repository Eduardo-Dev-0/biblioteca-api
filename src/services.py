
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.emprestimo_repository import EmprestimoRepository
from src.models import Emprestimo
from src.repositories import LivroRepository


class EmprestimoService:
    def __init__(
        self,
        livro_repository=None,
        emprestimo_repository=None
    ):
        self.livro_repository = livro_repository or LivroRepository()
        self.emprestimo_repository = (
            emprestimo_repository or EmprestimoRepository()
        )

    def realizar_emprestimo(
        self,
        db: Session,
        livro_id: int,
        leitor: str
    ):
        livro = self.livro_repository.buscar_por_id(db, livro_id)

        if livro is None:
            raise HTTPException(
                status_code=404,
                detail="Livro não encontrado."
            )

        if livro.quantidade_disponivel <= 0:
            raise HTTPException(
                status_code=400,
                detail="Livro indisponível para empréstimo."
            )

        emprestimo = Emprestimo(
            livro_id=livro_id,
            leitor=leitor
        )

        livro.quantidade_disponivel -= 1

        try:
            return self.emprestimo_repository.criar(db, emprestimo)
        except Exception:
            db.rollback()
            raise
