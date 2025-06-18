

# . Escopo da classe e de métodos da classe
class Animal:
# nome = 'Leão'
    def __init__(self, nome):
        self.nome = nome
        variavel = 'valor'
        print(variavel)

    def acao(self):
        print(f'{self.nome} está executando uma ação')

leao = Animal('Leão' )
print(leao.nome)
leao.acao()