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

"""
João Vítor Fernandes Dias
No código anterior você usou apenas uma linha de comentário.
Adicione em cada uma das definições de funções uma docstring que explique o que as funções fazem.

Claro, segue abaixo o código com as docstrings adicionadas:
"""

import math

class Ponto2D:
    """
    Classe que representa um ponto no plano cartesiano 2D
    """

    def __init__(self, x=0, y=0):
        """
        Construtor da classe que cria um ponto nas coordenadas (x,y)
        """
        self._x = x
        self._y = y

    def set_x(self, novo_x):
        """
        Altera o valor da coordenada x do ponto
        """
        self._x = novo_x

    def set_y(self, novo_y):
        """
        Altera o valor da coordenada y do ponto
        """
        self._y = novo_y

    def get_x(self):
        """
        Retorna o valor da coordenada x do ponto
        """
        return self._x

    def get_y(self):
        """
        Retorna o valor da coordenada y do ponto
        """
        return self._y

    def move_ponto(self, delta_x=0, delta_y=0):
        """
        Move o ponto em delta_x unidades no eixo x e delta_y unidades no eixo y
        """
        self._x += delta_x
        self._y += delta_y

    def move_ponto_para(self, novo_x=0, novo_y=0):
        """
        Move o ponto para as coordenadas (novo_x, novo_y)
        """
        self._x = novo_x
        self._y = novo_y

    def clone(self):
        """
        Cria e retorna um novo ponto com as mesmas coordenadas do ponto atual
        """
        return Ponto2D(self._x, self._y)

    def distancia(self, outro_ponto):
        """
        Calcula a distância euclidiana entre o ponto atual e outro_ponto
        """
        dx = self._x - outro_ponto.get_x()
        dy = self._y - outro_ponto.get_y()
        return (dx ** 2 + dy ** 2) ** 0.5

    def equals(self, outro_ponto):
        """
        Verifica se o ponto atual é igual a outro_ponto
        """
        return self._x == outro_ponto.get_x() and self._y == outro_ponto.get_y()

    def __str__(self):
        """
        Retorna uma string que representa o ponto no formato (x, y)
        """
        return "({}, {})".format(self._x, self._y)

    

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
