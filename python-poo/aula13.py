class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

caneta = Caneta('Azul')
# caneta.cor .= 'Rosa'
# print(caneta.cor)


