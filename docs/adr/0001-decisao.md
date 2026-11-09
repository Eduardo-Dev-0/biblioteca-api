# ADR 0001 — Decisões arquiteturais da Biblioteca API

- **Status:** Aceito
- **Data:** 09/11/2026
- **Projeto:** Biblioteca API

## 1. Contexto

O projeto Biblioteca API tem como objetivo desenvolver uma API REST para gerenciamento de livros e empréstimos.

A aplicação precisa permitir o cadastro e a consulta de livros, além da realização e consulta de empréstimos, respeitando a regra de disponibilidade de exemplares.

A arquitetura deve ser simples, organizada e adequada ao escopo acadêmico.

## 2. Decisões

### 2.1. Linguagem e framework

Foi escolhida a linguagem Python com o framework FastAPI para construção da API REST.

**Justificativa:** o FastAPI permite desenvolver endpoints de forma objetiva, oferece documentação automática com OpenAPI e facilita a validação dos dados.

### 2.2. Banco de dados

Foi escolhido SQLite para armazenamento dos livros e empréstimos.

**Justificativa:** oferece persistência de dados com configuração simples, sendo adequado ao escopo do projeto.

### 2.3. Padrão arquitetural

Foi escolhido o Repository Pattern para organizar o acesso aos dados.

**Justificativa:** separar as operações de persistência das regras de negócio facilita a manutenção, os testes e a organização do código.

A camada de serviços também é utilizada para concentrar as regras de negócio relacionadas aos empréstimos.

## 3. Consequências

- Estrutura de código organizada em responsabilidades.
- Separação entre acesso aos dados e regras de negócio.
- Facilidade para testar os componentes da aplicação.
- Menor complexidade de configuração utilizando SQLite.
- Possibilidade de substituir a implementação de persistência futuramente com menor impacto na camada de serviços.

## 4. Tecnologias utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- Docker e Docker Compose