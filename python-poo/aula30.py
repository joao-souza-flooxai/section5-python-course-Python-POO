#__new__ deve retornar outro objeto
#__init__ é o metodo responsavel por inicializar e não deve retornar nada
# object é o pai de class

class A:
    def __new__(cls):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self):
        print('Sou o init')

    def __repr__(self):
        return 'A()'

a = A()
print(a)