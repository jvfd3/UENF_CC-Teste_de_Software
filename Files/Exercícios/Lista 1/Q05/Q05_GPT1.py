'''

5. Escreva o programa Ponto2D que represente um ponto no plano cartesiano. Além dos atributos por você identificados, a classe deve oferecer os seguintes membros:
   a. Construtores sobrecarregados que permitam a inicialização do ponto:
      1. Por default (sem parâmetros) na origem do espaço 2D;
      2. Num local indicado por dois parâmetros do tipo double (indicando o valor de abcissa e ordenada do ponto que está sendo criado);
      3. Em um local indicado por outro ponto.

   b. Métodos de acesso (getter/setter) dos atributos do ponto;
   c. Métodos sobrecarregados de movimentação do ponto com os mesmos parâmetros indicados para os construtores;
   d. Método de comparação semântica do ponto (equals);
   e. Método de representação do objeto como String;
   f. Método que permita calcular a distância do ponto que recebe a mensagem, para outro ponto;
   g. Método que permita a criação de um novo ponto no mesmo local do ponto que recebeu a mensagem (clone);

'''

import math

class Ponto2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
        
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y
        
    def mover_pelo_ponto(self, outro_ponto):
        self.x = outro_ponto.x
        self.y = outro_ponto.y
        
    def mover_pelas_coordenadas(self, x, y):
        self.x = x
        self.y = y
        
    def mover_horizontalmente(self, dx):
        self.x += dx
        
    def mover_verticalmente(self, dy):
        self.y += dy
        
    def equals(self, outro_ponto):
        return self.x == outro_ponto.x and self.y == outro_ponto.y
        
    def clone(self):
        return Ponto2D(self.x, self.y)
        
    def distancia(self, outro_ponto):
        dx = self.x - outro_ponto.x
        dy = self.y - outro_ponto.y
        return math.sqrt(dx*dx + dy*dy)
    

# testando a classe
p1 = Ponto2D()
p2 = Ponto2D(3.0, 4.0)
p3 = Ponto2D()
p3.mover_pelas_coordenadas(-1.0, 2.0)

assert p1.get_x() == 0.0
assert p1.get_y() == 0.0

assert p2.get_x() == 3.0
assert p2.get_y() == 4.0

assert p3.get_x() == -1.0
assert p3.get_y() == 2.0

p1.set_x(1.0)
p1.set_y(2.0)

assert p1.get_x() == 1.0
assert p1.get_y() == 2.0

p1.mover_pelo_ponto(p2)

assert p1.get_x() == 3.0
assert p1.get_y() == 4.0

p1.mover_horizontalmente(-2.0)

assert p1.get_x() == 1.0
assert p1.get_y() == 4.0

p1.mover_verticalmente(-3.0)

assert p1.get_x() == 1.0
assert p1.get_y() == 1.0

assert p1.equals(Ponto2D(1.0, 1.0))
assert not p1.equals(p2)

p4 = p2.clone()

assert p4.get_x() == 3.0
assert p4.get_y() == 4.0

assert p1.distancia(p2) == p2.distancia(p1)

assert math.isclose(p1.distancia(p2), math.sqrt(10), rel_tol=1e-9)

"""
Neste código, criamos a classe Ponto2D que representa um ponto no plano cartesiano. A classe possui três construtores sobrecarregados, que permitem a inicialização do ponto: por default (sem parâmetros) na origem do espaço 2D, num local indicado por dois parâmetros do tipo double (indicando o valor de abcissa e ordenada do ponto que está sendo criado) ou em um local indicado por outro ponto
"""
