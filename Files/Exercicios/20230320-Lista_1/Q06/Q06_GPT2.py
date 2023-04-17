'''

6. Considere que uma biblioteca gráfica disponibiliza uma classe Visual os métodos da Tabela 1. A partir desta biblioteca:
   a. Escreve uma classe que seja capaz de armazenar o estado e plotar um objeto geométrico (plotar no caso seria imprimir os vértices e no caso de um círculo as coordenadas do centro e seu raio).
   b. Defina uma interface única para desenhar os objetos e crie uma classe que permita agregar objetos geométricos simples (linha, retângulo e círculo) e compostos (objetos que já agregam outros objetos). (Leia sobre o padrão de projeto composite)
   c. Escreva uma fábrica (leia sobre o padrão de projeto Factory) para construir objetos simples (um único método) e compostos (outro método).

#### Tabela 1

| Função | Descrição | Variáveis |
|------|-----------|---|
| drawLine(x1, y1, x2, y2) | Desenha uma linha. | x1 e y1 - coordenadas do ponto de origem; x2 e y2 - coordenadas do ponto de destino. |
| drawRectangle(x, y, altura, largura) | Desenha um retângulo. | x e y - coordenadas do canto esquerdo superior; altura e largura do retângulo. |
| drawCircle(x, y, raio) | Desenha um círculo. | x e y - coordenadas do centro; raio - raio do círculo. |

'''

"""
João Vítor Fernandes Dias
Você se esqueceu mais uma vez dos testes e docstrings. Por favor, reescreva seu código

Desculpe pelo erro. Aqui está o código com testes e docstrings:
"""
from abc import ABC, abstractmethod

# Tabela 1: Funções da classe Visual
class Visual:
    def drawLine(self, x1, y1, x2, y2):
        print(f"Desenhando uma linha de ({x1},{y1}) até ({x2},{y2})")

    def drawRectangle(self, x, y, altura, largura):
        print(f"Desenhando um retângulo no ponto ({x},{y}) com altura {altura} e largura {largura}")

    def drawCircle(self, x, y, raio):
        print(f"Desenhando um círculo com centro em ({x},{y}) e raio {raio}")


# Classe para armazenar o estado e plotar um objeto geométrico
class GeometricObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self):
        """
        Plota o objeto geométrico.
        """
        pass  # implementação da plotagem de cada objeto será feita nas classes derivadas


class Line(GeometricObject):
    def __init__(self, x1, y1, x2, y2):
        """
        Cria um objeto do tipo linha.

        :param x1: coordenada x do ponto inicial da linha.
        :param y1: coordenada y do ponto inicial da linha.
        :param x2: coordenada x do ponto final da linha.
        :param y2: coordenada y do ponto final da linha.
        """
        super().__init__(x1, y1)
        self.x2 = x2
        self.y2 = y2

    def plot(self):
        """
        Plota a linha.
        """
        Visual().drawLine(self.x, self.y, self.x2, self.y2)


class Rectangle(GeometricObject):
    def __init__(self, x, y, altura, largura):
        """
        Cria um objeto do tipo retângulo.

        :param x: coordenada x do canto esquerdo superior do retângulo.
        :param y: coordenada y do canto esquerdo superior do retângulo.
        :param altura: altura do retângulo.
        :param largura: largura do retângulo.
        """
        super().__init__(x, y)
        self.altura = altura
        self.largura = largura

    def plot(self):
        """
        Plota o retângulo.
        """
        Visual().drawRectangle(self.x, self.y, self.altura, self.largura)


class Circle(GeometricObject):
    def __init__(self, x, y, raio):
        """
        Cria um objeto do tipo círculo.

        :param x: coordenada x do centro do círculo.
        :param y: coordenada y do centro do círculo.
        :param raio: raio do círculo.
        """
        super().__init__(x, y)
        self.raio = raio

    def plot(self):
        """
        Plota o círculo.
        """
        Visual().drawCircle(self.x, self.y, self.raio)


# Interface para desenhar objetos geométricos
class Drawable(ABC):
    @abstractmethod
    def plot(self):
        pass


# Classe para agregar objetos geométricos simples e compostos
class
