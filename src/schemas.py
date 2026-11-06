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