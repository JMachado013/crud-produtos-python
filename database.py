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

def excluir_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))

    conexao.commit()
    conexao.close()

def editar_produto(id_produto, nome, descricao, preco, quantidade, categoria):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE produtos
    SET nome = ?, descricao = ?, preco = ?, quantidade = ?, categoria = ?
    WHERE id = ?
    """, (nome, descricao, preco, quantidade, categoria, id_produto))

    conexao.commit()
    conexao.close()