#Usando o construtor(__init__) na classe.

class Pessoa:
    #self é a referência para o objeto que chamou a classe(p1,p2)
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
p1 = Pessoa('Luiz','Otávio')
p2 = Pessoa('Maria','Joana')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
