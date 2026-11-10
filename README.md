# Biblioteca API

API REST desenvolvida em Python com FastAPI para gerenciamento de livros e empréstimos de uma biblioteca.

Projeto acadêmico desenvolvido com foco na aplicação de princípios SOLID, Repository Pattern, testes automatizados, documentação e integração contínua.

## 1. Escopo do projeto

A API permite:

- Cadastrar livros.
- Listar livros cadastrados.
- Consultar um livro pelo identificador.
- Realizar empréstimos de livros disponíveis.
- Consultar empréstimos realizados.

### Regra de negócio

Não é permitido realizar empréstimos quando o livro não possui exemplares disponíveis.

## 2. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.12 | Linguagem |
| FastAPI | Desenvolvimento da API |
| SQLite | Banco de dados |
| SQLAlchemy | ORM e persistência |
| Pydantic | Validação de dados |
| Pytest | Testes automatizados |
| pytest-cov | Cobertura de testes |
| Ruff | Qualidade de código |
| Docker | Containerização |
| Docker Compose | Orquestração |
| GitHub Actions | Integração contínua |
| k6 | Teste de desempenho |

## 3. Arquitetura e padrões

O projeto utiliza o **Repository Pattern**, separando as operações de persistência das demais responsabilidades da aplicação.

A camada de serviços concentra regras de negócio, como a validação da disponibilidade de livros antes de realizar um empréstimo.

Essa organização facilita a manutenção, os testes e a evolução do sistema.

## 4. Como executar o projeto

### Opção A — Docker Compose (recomendada)

É necessário ter o Docker Desktop instalado e em execução.

Na raiz do projeto, execute:

```bash
docker compose up --build
```

A API estará disponível em:

http://localhost:8000

Para acessar a documentação interativa:

http://localhost:8000/docs

Para encerrar:

```bash
docker compose down
```

Os dados do banco SQLite são armazenados em um volume Docker, permitindo sua persistência entre reinicializações dos containers.

### Opção B — Execução local

É necessário ter Python 3.12 instalado.

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a API:

```bash
uvicorn src.main:app --reload
```

A aplicação estará disponível em:

http://localhost:8000

## 5. Endpoints principais

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verificar funcionamento |
| GET | `/livros` | Listar livros |
| POST | `/livros` | Cadastrar livro |
| GET | `/livros/{livro_id}` | Consultar livro |
| POST | `/emprestimos` | Realizar empréstimo |
| GET | `/emprestimos/{emprestimo_id}` | Consultar empréstimo |
| GET | `/metrics` | Consultar métricas |

A especificação completa está disponível em `docs/openapi.yaml`.

## 6. Testes automatizados

O projeto utiliza Pytest para validar os principais comportamentos da API.

Para executar os testes:

```bash
python -m pytest -v
```

A cobertura mínima exigida está configurada em 70% no arquivo `pytest.ini`.

Para executar e visualizar o relatório de cobertura:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

## 7. Qualidade de código

A ferramenta Ruff é utilizada para verificar a qualidade e a organização do código.

Execute:

```bash
ruff check src tests
```

## 8. Integração contínua

O projeto utiliza GitHub Actions para executar automaticamente:

- Instalação das dependências.
- Verificação de código com Ruff.
- Execução dos testes automatizados com Pytest.
- Verificação do limite mínimo de cobertura.

O workflow está localizado em `.github/workflows/ci.yml`.

## 9. Desempenho e monitoramento

O projeto possui um smoke test desenvolvido com k6.

O cenário avaliado utiliza um usuário virtual durante 10 segundos, com meta de p95 inferior a 500 ms e taxa de falhas inferior a 1%.

O SLO definido é de 95% das requisições em até 500 ms.

Os registros de requisições são emitidos em formato JSON, contendo método, caminho, código HTTP e duração.

As métricas podem ser consultadas pelo endpoint `/metrics`.

Os resultados do teste estão documentados em `docs/desempenho.md`.

## 10. Documentação adicional

- `docs/adr/0001-decisao.md` — registro das decisões arquiteturais.
- `docs/c4/contexto.md` — diagrama de contexto C4.
- `docs/openapi.yaml` — especificação OpenAPI.
- `docs/desempenho.md` — plano e resultados do teste de desempenho.
- `docs/ia.md` — registro de utilização de inteligência artificial.

## 11. Escopo acadêmico

Esta versão contempla um domínio único, com funcionalidades essenciais de cadastro, consulta e empréstimo de livros.

Funcionalidades adicionais, como autenticação, reservas, multas e notificações, não fazem parte do escopo desta entrega.