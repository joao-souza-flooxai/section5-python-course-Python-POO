# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.

class Carrinho:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self. produtos.append(produto)

    def total(self):
        return sum([p.preco for p in self. produtos])

    def listar_produtos(self):
        print()
        for produto in self. produtos:
            print(produto.nome, produto.preco)
            print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta',1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
