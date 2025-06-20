# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamif@ro -> Humano ->Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa .- > Cliente
# Cliente(Pessoa, FileLog)

class A:
    
    def quem_sou(self):
        print('A')

class B(A):
    
    def quem_sou(self):
        print('B')

class C(A):
    
    def quem_sou(self):
        print('C')

class D(B, C):
    
    def quem_sou(self):
        print('D')

d = D()
d.quem_sou()