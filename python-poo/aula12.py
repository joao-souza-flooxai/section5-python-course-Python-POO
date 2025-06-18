# @property - um getter em Python
# getter - um método para obter um atributo
# cor -> getrcor()

# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo


# Maneira tradicional:
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    def get_cor(self):
        print('GET COR tradicional')
        return self.cor_tinta

caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())


#Em python:

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        
    @property
    def cor(self):
        print('GET COR com property')
        return self.cor_tinta

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)