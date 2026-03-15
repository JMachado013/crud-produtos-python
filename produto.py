class Produto:
    def __init__(self, nome, descricao, preco, quantidade, categoria):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Descrição:", self.descricao)
        print("Preço:", self.preco)
        print("Quantidade:", self.quantidade)
        print("Categoria:", self.categoria)