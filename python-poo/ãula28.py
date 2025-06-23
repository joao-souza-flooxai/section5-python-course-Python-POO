# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y):
        self.x =x
        self.y =y

    #Resposta padrão de str dessa classe
    def __str__(self):
        return f'({self.x}, {self.y})'

    #Se str não estiver definido, vai para repr

    #Para desenvolvedor:
    def __repr__(self):
        #class_name = self.__class__.name__
        class_name = type(self).__name__
        return f'Veio da classe: {class_name},  com os atributos:{self.x!r}, {self.y!r}'


p1 = Ponto(1,2)
p2= Ponto(978, 876)
print(p1)
print(repr(p2))
print(f'{p1!r}')