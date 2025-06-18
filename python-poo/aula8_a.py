# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula8.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def toJson(self):
        return {"nome": self.nome, "idade": self.idade}

p1 = Pessoa( 'Joao', 33)
p2= Pessoa('Helena',21)
p3 = Pessoa('Joana',11)
bd=[vars(p1),vars(p2),vars(p3)]

def salvar():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd,arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__': 
    salvar()