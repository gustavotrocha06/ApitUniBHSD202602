# API de Registros: do Monolito para Multicamadas

**Nome:** Gustavo Teixeira Rocha Araujo
**Disciplina/Atividade:** Do monolito para multicamadas
**Repositório original:** https://github.com/fvaladares/ApitUniBHSD202602

## 1. Ponto de partida

API REST (FastAPI + SQLite) com CRUD de `/registros`, toda concentrada em um único arquivo (`App.py`): conexão com o banco, modelos Pydantic e rotas.

## 2. O que foi feito

1. Fork do repositório original e criação da branch `multicamadas`.
2. Execução do monolito e teste de todas as rotas no Swagger (`/docs`), para ter uma referência do comportamento original.
3. Divisão do código em camadas, sem alterar as regras nem as rotas:

| Arquivo | Responsabilidade | O que foi movido |
|---|---|---|
| `database.py` | Acesso ao banco | `get_db_connection` (renomeada `conectar_banco`) e a criação da tabela (`criar_tabelas`) |
| `models.py` | Contratos de dados | Classes `RegistroBase` e `RegistroResponse` |
| `main.py` | Rotas HTTP | `FastAPI()` e os endpoints, que importam `database` e `models` |

4. Renomeação de `App.py` para `main.py`, seguindo o guia do README original.
5. Inclusão de `.gitignore` para não versionar `banco_a3.db`, `__pycache__/` e `.venv/`.

## 3. Estrutura final

```
.
├── database.py
├── models.py
├── main.py
├── pyproject.toml
└── README.md
```

## 4. Como executar

```
pip install uv
uv add fastapi uvicorn
uv run uvicorn main:app --reload
```

Documentação interativa: `http://127.0.0.1:8000/docs`

## 5. Endpoints (inalterados)

| Método | Rota | Resposta |
|---|---|---|
| POST | `/registros` | 201 ou 400 |
| GET | `/registros` | 200 |
| GET | `/registros/{id}` | 200 ou 404 |
| PUT | `/registros/{id}` | 200 ou 404 |
| DELETE | `/registros/{id}` | 200 ou 404 |

## 6. Validação

Todas as rotas foram testadas no Swagger antes e depois da refatoração, com o mesmo resultado.

## 7. Problemas encontrados

- O README original citava `main.py`, mas o arquivo se chamava `App.py`; o comando de execução foi ajustado.
- Os arquivos novos ficaram em uma subpasta duplicada no Codespaces; foram movidos para a raiz.
