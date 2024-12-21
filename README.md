# BoilerPlate de um WebService utilizando FastApi

> Um webservice em FastApi

[![Python Version][python-image]][python-url]
[![FastApi][fastapi-image]][fastApi-url]
![Coverage][coverage-image]

<p>Criado em Python na versão 3.12 junto ao framework FastApi.</p>

## Pacotes

Segue a lista de pacotes utilizados no projeto.

| Package                  | Version |
| ------------------------ | ------- |
| [FastApi][fastApi-url]   | 0.109.2 |
| [Uvicorn][uvicorn-url]   | 0.27.1  |
| [Pydantic][pydantic-url] | 2.6.1   |

## Requisitos

- Python 3.12
- Docker & Docker Compose

## Configuração Inicial

1. Clone o repositório:

   ```sh
   git clone https://github.com/UdsonWillams/challenger
   ```

2. Crie o arquivo `.env` com base no `.env.example`:

   ```sh
   cp .env.example .env
   ```

3. Atualize as variáveis de ambiente no arquivo `.env` conforme necessário. Caso não seja criado um arquivo `.env` o projeto não iniciará via compose.

## Executando a Aplicação

1. Construa e inicie os contêineres Docker:

   ```sh
   docker-compose up --build
   ```

2. Acesse a aplicação em `http://localhost:8000`.

### Executando a Aplicação (Localmente sem Docker)

1. Localmente com seu ambiente python, instale a lista de pacotes.

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requeriments-dev.txt
```

2. Após isso utilize o comando:

```sh
uvicorn app.main:app
OU
# Caso você possua o make instalado
make runserver
# Caso não tenha, você pode instalar por meio do comando: sudo apt install make
```

3. Com isso o projeto já estará funcionando.

## Exemplo de uso:

Podemos utiliza-lo para fazermos os testes no projeto, ou apenas para pegar os valores
de referencia para utilização em um

Exemplo dos endpoints:

```sh
/api/v1/words/sort :: para retorno das palavras ordenado
/api/v1/words/vowel_count :: para contagem das vogais das palavras passadas.
```

## Documentação da API

A aplicação possui Swagger para documentação da API. Acesse a documentação em `http://localhost:8000/swagger/`.

## Testes

Para rodar os testes, use o seguinte comando:

```sh
make coverage
```

## Ferramentas de Desenvolvimento

Esta aplicação utiliza as seguintes ferramentas de desenvolvimento:

- pre-commit para hooks de commit
- Ruff para linting e formatação de código
- ipdb para debugging


<!-- Markdown link & img dfn's -->

[python-image]: https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
[fastApi-image]: https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi
[fastApi-url]: https://fastapi.tiangolo.com/
[uvicorn-url]: https://www.uvicorn.org/
[pydantic-url]: https://docs.pydantic.dev/latest/
[fastapi-image]: https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi
[coverage-image]: https://coverage-badge.samuelcolvin.workers.dev/tiangolo/fastapi.svg
