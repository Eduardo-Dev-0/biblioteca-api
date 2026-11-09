from datetime import datetime

from pydantic import BaseModel, Field


class LivroCreate(BaseModel):
    titulo: str
    autor: str
    quantidade_disponivel: int = Field(default=1, ge=1)


class LivroResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    quantidade_disponivel: int

    model_config = {"from_attributes": True}


class EmprestimoCreate(BaseModel):
    livro_id: int
    leitor: str = Field(min_length=2)


class EmprestimoResponse(BaseModel):
    id: int
    livro_id: int
    leitor: str
    data_emprestimo: datetime

    model_config = {"from_attributes": True}
