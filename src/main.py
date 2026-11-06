from fastapi import FastAPI

app = FastAPI(
    title="Biblioteca API",
    description="API para gerenciamento de livros e empréstimos.",
    version="1.0.0"
)


@app.get("/")
def inicio():
    return {"mensagem": "Biblioteca API funcionando!"}


@app.get("/livros")
def listar_livros():
    return []