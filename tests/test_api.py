
def test_api_esta_funcionando(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert resposta.json() == {
        "mensagem": "Biblioteca API funcionando!"
    }


def test_cadastrar_livro(client):
    resposta = client.post(
        "/livros",
        json={
            "titulo": "Python para Iniciantes",
            "autor": "Autor Teste",
            "quantidade_disponivel": 3
        }
    )

    assert resposta.status_code == 201

    dados = resposta.json()

    assert dados["titulo"] == "Python para Iniciantes"
    assert dados["autor"] == "Autor Teste"
    assert dados["quantidade_disponivel"] == 3
    assert "id" in dados


def test_listar_livros(client):
    client.post(
        "/livros",
        json={
            "titulo": "Livro de Teste",
            "autor": "Autor Teste",
            "quantidade_disponivel": 2
        }
    )

    resposta = client.get("/livros")

    assert resposta.status_code == 200
    assert len(resposta.json()) == 1
    assert resposta.json()[0]["titulo"] == "Livro de Teste"


def test_buscar_livro_por_id(client):
    cadastro = client.post(
        "/livros",
        json={
            "titulo": "Livro de Consulta",
            "autor": "Autor Teste",
            "quantidade_disponivel": 1
        }
    )

    livro_id = cadastro.json()["id"]

    resposta = client.get(f"/livros/{livro_id}")

    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Livro de Consulta"


def test_buscar_livro_inexistente(client):
    resposta = client.get("/livros/9999")

    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Livro não encontrado."


def test_cadastrar_livro_com_quantidade_invalida(client):
    resposta = client.post(
        "/livros",
        json={
            "titulo": "Livro Inválido",
            "autor": "Autor Teste",
            "quantidade_disponivel": 0
        }
    )

    assert resposta.status_code == 422


def test_realizar_emprestimo(client):
    cadastro = client.post(
        "/livros",
        json={
            "titulo": "Python Avançado",
            "autor": "Autor Teste",
            "quantidade_disponivel": 2
        }
    )

    livro_id = cadastro.json()["id"]

    resposta = client.post(
        "/emprestimos",
        json={
            "livro_id": livro_id,
            "leitor": "João da Silva"
        }
    )

    assert resposta.status_code == 201
    assert resposta.json()["livro_id"] == livro_id
    assert resposta.json()["leitor"] == "João da Silva"

    livro_atualizado = client.get(f"/livros/{livro_id}")

    assert livro_atualizado.json()["quantidade_disponivel"] == 1


def test_impedir_emprestimo_sem_disponibilidade(client):
    cadastro = client.post(
        "/livros",
        json={
            "titulo": "Livro Único",
            "autor": "Autor Teste",
            "quantidade_disponivel": 1
        }
    )

    livro_id = cadastro.json()["id"]

    # Primeiro empréstimo: deve funcionar.
    primeiro_emprestimo = client.post(
        "/emprestimos",
        json={
            "livro_id": livro_id,
            "leitor": "Leitor Um"
        }
    )

    assert primeiro_emprestimo.status_code == 201

    # Segundo empréstimo: deve ser recusado.
    segundo_emprestimo = client.post(
        "/emprestimos",
        json={
            "livro_id": livro_id,
            "leitor": "Leitor Dois"
        }
    )

    assert segundo_emprestimo.status_code == 400
    assert segundo_emprestimo.json()["detail"] == (
        "Livro indisponível para empréstimo."
    )


def test_impedir_emprestimo_de_livro_inexistente(client):
    resposta = client.post(
        "/emprestimos",
        json={
            "livro_id": 9999,
            "leitor": "Leitor Teste"
        }
    )

    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Livro não encontrado."


def test_consultar_emprestimo(client):
    cadastro = client.post(
        "/livros",
        json={
            "titulo": "Livro para Consulta",
            "autor": "Autor Teste",
            "quantidade_disponivel": 1
        }
    )

    livro_id = cadastro.json()["id"]

    emprestimo = client.post(
        "/emprestimos",
        json={
            "livro_id": livro_id,
            "leitor": "Leitor Consulta"
        }
    )

    emprestimo_id = emprestimo.json()["id"]

    resposta = client.get(f"/emprestimos/{emprestimo_id}")

    assert resposta.status_code == 200
    assert resposta.json()["id"] == emprestimo_id
    assert resposta.json()["leitor"] == "Leitor Consulta"
