import sqlite3

DB_NAME = "banco_a3.db"


def conectar_banco():
    # Cria o arquivo banco_a3.db na mesma pasta do projeto
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn


def criar_tabelas():
    conn = conectar_banco()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            ativo BOOLEAN DEFAULT TRUE
        )
    ''')
    conn.commit()
    conn.close()