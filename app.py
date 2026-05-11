from flask import Flask, render_template, request, redirect
from produto import Produto
from database import criar_tabela, inserir_produto, listar_produtos, excluir_produto, editar_produto

app = Flask(__name__)

criar_tabela()

@app.route("/")
def index():
    produtos = listar_produtos()
    return render_template("index.html", produtos=produtos)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    preco = float(request.form["preco"])
    quantidade = int(request.form["quantidade"])
    categoria = request.form["categoria"]

    produto = Produto(nome, descricao, preco, quantidade, categoria)
    inserir_produto(produto)

    return redirect("/")

@app.route("/excluir/<int:id_produto>")
def excluir(id_produto):
    excluir_produto(id_produto)
    return redirect("/")

@app.route("/editar/<int:id_produto>", methods=["POST"])
def editar(id_produto):
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    preco = float(request.form["preco"])
    quantidade = int(request.form["quantidade"])
    categoria = request.form["categoria"]

    editar_produto(id_produto, nome, descricao, preco, quantidade, categoria)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)