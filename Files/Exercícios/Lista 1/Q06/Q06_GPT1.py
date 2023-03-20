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
Para atender ao exercício, segue abaixo uma possível implementação das classes solicitadas:
"""

from abc import ABC, abstractmethod

class Visual:
    def __init__(self):
        self.vertices = []
    
    def add_vertex(self, x, y):
        self.vertices.append((x, y))

    @abstractmethod
    def draw(self):
        pass

class GeometricObject(Visual):
    def __init__(self, *args):
        super().__init__()
        for arg in args:
            self.add_vertex(*arg)

class Line(GeometricObject):
    def __init__(self, x1, y1, x2, y2):
        super().__init__((x1, y1), (x2, y2))

    def draw(self):
        print("Linha:")
        for v in self.vertices:
            print(v)

class Rectangle(GeometricObject):
    def __init__(self, x, y, altura, largura):
        super().__init__((x, y), (x + largura, y), (x + largura, y + altura), (x, y + altura))

    def draw(self):
        print("Retângulo:")
        for v in self.vertices:
            print(v)

class Circle(Visual):
    def __init__(self, x, y, raio):
        super().__init__()
        self.centro = (x, y)
        self.raio = raio

    def draw(self):
        print("Círculo:")
        print("Centro:", self.centro)
        print("Raio:", self.raio)

class Composite(Visual):
    def __init__(self, *args):
        super().__init__()
        for obj in args:
            self.add_vertex(*obj.centro)
            self.vertices.extend(obj.vertices)

    def draw(self):
        print("Composto:")
        for v in self.vertices:
            print(v)

class GeometricObjectFactory:
    @staticmethod
    def create_line(x1, y1, x2, y2):
        return Line(x1, y1, x2, y2)

    @staticmethod
    def create_rectangle(x, y, altura, largura):
        return Rectangle(x, y, altura, largura)

    @staticmethod
    def create_circle(x, y, raio):
        return Circle(x, y, raio)

class CompositeFactory:
    @staticmethod
    def create_composite(*args):
        return Composite(*args)


"""
Explicação:

Visual: classe base abstrata que representa um objeto visual genérico, que possui um conjunto de vértices;
GeometricObject: classe que herda de Visual e representa um objeto geométrico, que é definido a partir de um conjunto de pontos (vértices);
Line, Rectangle, Circle: subclasses de GeometricObject que representam objetos geométricos simples (linha, retângulo e círculo, respectivamente), e que implementam o método abstrato draw da classe Visual, que imprime os vértices do objeto na tela;
Composite: classe que herda de Visual e representa um objeto geométrico composto, que é definido a partir de um conjunto de outros objetos geométricos (simples ou compostos), e que implementa o método draw da classe Visual, que imprime os vértices de todos os objetos agregados na tela;
GeometricObjectFactory, CompositeFactory: classes que implementam o padrão de projeto Factory, que são responsáveis por criar objetos geométricos
"""
