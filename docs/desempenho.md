
# Plano de Desempenho — Biblioteca API

## 1. Objetivo

Avaliar o tempo de resposta e a estabilidade da Biblioteca API
por meio de um teste simples de desempenho utilizando k6.

## 2. Ferramenta

- Ferramenta: k6
- Execução: container Docker
- Ambiente: aplicação executada via Docker Compose.

## 3. Cenário de teste

O teste realiza requisições HTTP GET ao endpoint `/livros`.

Configuração:
- Usuários virtuais: 1
- Duração: 10 segundos
- Endpoint: GET /livros
- Resposta esperada: HTTP 200

## 4. Indicadores avaliados

- p95: percentil 95 do tempo de resposta.
- Taxa de falhas: percentual de requisições com erro.
- Quantidade de requisições realizadas.

## 5. Metas de desempenho

- p95 inferior a 500 ms.
- Taxa de falhas inferior a 1%.

## 6. Resultado do teste


## 6. Resultado do teste

O smoke test foi executado utilizando k6, com a API
hospedada em Docker.

### Configuração executada

- Endpoint: GET /livros
- Usuários virtuais: 1
- Duração: 10 segundos
- Total de requisições: 3.330

### Resultados obtidos

| Indicador | Resultado | Meta |
|---|---:|---:|
| p95 | 3,78 ms | < 500 ms |
| Taxa de falhas | 0,00% | < 1% |
| Tempo médio | 2,90 ms | — |
| Tempo máximo | 12,87 ms | — |
| Requisições por segundo | 333,00 | — |
| Checks aprovados | 100% | 100% |

### Avaliação

O teste foi aprovado.

O percentil 95 ficou abaixo do limite de 500 ms
e não foram registradas falhas nas requisições.

## 7. Conclusão

O smoke test demonstrou que a Biblioteca API
apresentou bom desempenho no cenário local avaliado.

As metas definidas para o teste foram atingidas:

- p95 inferior a 500 ms.
- Taxa de falhas inferior a 1%.

Os resultados são válidos para o cenário testado,
com um usuário virtual durante 10 segundos.

Testes com maior concorrência e em ambiente
de produção seriam necessários para avaliar
o comportamento sob cargas mais elevadas.