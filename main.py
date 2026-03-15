from produto import Produto
from database import criar_tabela, inserir_produto, listar_produtos

criar_tabela()

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição: ")
        preco = float(input("Digite o preço: "))
        quantidade = int(input("Digite a quantidade: "))
        categoria = input("Digite a categoria: ")

        produto = Produto(nome, descricao, preco, quantidade, categoria)
        inserir_produto(produto)

        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        produtos = listar_produtos()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            print("\n=== LISTA DE PRODUTOS ===")
            for produto in produtos:
                print(produto)

    elif opcao == "3":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")