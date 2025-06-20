# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso

# Mas podemos seguir as seguintes convenções:
# Sem underline = public
# 1 underline = protected
# 2 underlines = private

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self__private = 'isso é private'

    def metodo_publico(self):
        print(self.public)
    
    def _metodo_protected(self):
        print(self._protected)
    
    def __metodo_private(self):
        print(self__private)


f = Foo()
print(f._protected)
# print(f.public)
# print(f.metodo_publico())

