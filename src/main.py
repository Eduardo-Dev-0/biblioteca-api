
import json
import logging
import time

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

from src.database import Base, SessionLocal, engine
from src.emprestimo_repository import EmprestimoRepository
from src.repositories import LivroRepository
from src.schemas import (
    EmprestimoCreate,
    EmprestimoResponse,
    LivroCreate,
    LivroResponse,
)
from src.services import EmprestimoService

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Biblioteca API",
    description="API para gerenciamento de livros e empréstimos.",
    version="1.0.0"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("biblioteca-api")

metricas = {
    "total_requisicoes": 0,
    "requisicoes_ate_500ms": 0
}

livro_repository = LivroRepository()
emprestimo_repository = EmprestimoRepository()
emprestimo_service = EmprestimoService()


@app.middleware("http")
async def registrar_requisicao(request: Request, call_next):
    inicio = time.perf_counter()

    response = await call_next(request)

    duracao = (time.perf_counter() - inicio) * 1000

    if request.url.path != "/metrics":
        metricas["total_requisicoes"] += 1

        if duracao <= 500:
            metricas["requisicoes_ate_500ms"] += 1

    log = {
        "metodo": request.method,
        "caminho": request.url.path,
        "status_code": response.status_code,
        "duracao_ms": round(duracao, 2)
    }

    logger.info(json.dumps(log, ensure_ascii=False))

    return response


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def inicio():
    return {"mensagem": "Biblioteca API funcionando!"}


@app.get("/livros", response_model=list[LivroResponse])
def listar_livros(db: Session = Depends(get_db)):
    return livro_repository.listar(db)


@app.post("/livros", response_model=LivroResponse, status_code=201)
def cadastrar_livro(
    livro: LivroCreate,
    db: Session = Depends(get_db)
):
    return livro_repository.criar(db, livro)


@app.get(
    "/livros/{livro_id}",
    response_model=LivroResponse,
    responses={
        404: {"description": "Livro não encontrado"}
    }
)
def buscar_livro(
    livro_id: int,
    db: Session = Depends(get_db)
):
    livro = livro_repository.buscar_por_id(db, livro_id)

    if livro is None:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado."
        )

    return livro


@app.post(
    "/emprestimos",
    response_model=EmprestimoResponse,
    status_code=201,
    responses={
        400: {"description": "Livro indisponível para empréstimo"},
        404: {"description": "Livro não encontrado"}
    }
)
def realizar_emprestimo(
    dados: EmprestimoCreate,
    db: Session = Depends(get_db)
):
    return emprestimo_service.realizar_emprestimo(
        db,
        dados.livro_id,
        dados.leitor
    )


@app.get(
    "/emprestimos/{emprestimo_id}",
    response_model=EmprestimoResponse,
    responses={
        404: {"description": "Empréstimo não encontrado"}
    }
)
def buscar_emprestimo(
    emprestimo_id: int,
    db: Session = Depends(get_db)
):
    emprestimo = emprestimo_repository.buscar_por_id(
        db,
        emprestimo_id
    )

    if emprestimo is None:
        raise HTTPException(
            status_code=404,
            detail="Empréstimo não encontrado."
        )

    return emprestimo


@app.get("/metrics")
def consultar_metricas():
    total = metricas["total_requisicoes"]
    dentro_limite = metricas["requisicoes_ate_500ms"]

    percentual = (
        (dentro_limite / total) * 100
        if total > 0 else 0
    )

    return {
        "total_requisicoes": total,
        "requisicoes_ate_500ms": dentro_limite,
        "percentual_ate_500ms": round(percentual, 2)
    }
