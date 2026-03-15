import sqlite3

def conectar():
    conexao = sqlite3.connect("produtos.db")
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL,
        quantidade INTEGER,
        categoria TEXT
    )
    """)

    conexao.commit()
    conexao.close()

def inserir_produto(produto):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO produtos (nome, descricao, preco, quantidade, categoria)
    VALUES (?, ?, ?, ?, ?)
        """, (
    produto.nome,
    produto.descricao,
    produto.preco,
    produto.quantidade,
    produto.categoria
    ))

    conexao.commit()
    conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    conexao.close()
    return produtos