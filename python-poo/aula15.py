# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.


class Escritor:
 def  __init__(self, nome) ->None:
    self.nome = nome


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self. ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self. ferramenta = ferramenta


    class FerramentaDeEscrever:
        def __init__(self, nome):
            self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'
    
escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor. ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor. ferramenta.escrever())

