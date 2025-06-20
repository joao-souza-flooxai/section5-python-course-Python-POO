# Exercício com classes
# 1- Crie uma classe Carro (Nome)
# 2- Crie uma classe Motor (Nome)
# 3- Crie uma classe Fabricante (Nome)
# 4- Faça a ligação entre Carlo tem Motor
# Obs: Um motor pode ser de varios carros
# 5- Faça a ligação entre Carro e Fabricante
# Obs: Um fabricante pode fabricar varios carros
# Exiba o nome do carro, motor e fabricantes na tela

class Carro:
    def __init__(self, nome, motor):
        self.nome = nome
        self.motor = Motor(motor)

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []
    
    def produzir_carros(self, *carros):
        for carro in carros:
            self.carros.append(carro)
    def listar_carros(self):
        for carro in self.carros:
            print(carro.nome, carro.motor.nome)

carro_f1 = Carro('Celta', 'v8')
fabricante_1 = Fabricante('Lolinha')
fabricante_1.produzir_carros(carro_f1) 
fabricante_1.listar_carros()