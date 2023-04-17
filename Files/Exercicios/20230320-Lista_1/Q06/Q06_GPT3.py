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
Seu código ainda não teve os asserts para testagem do código, por favor, reescreva seu código.

Claro, segue abaixo o código novamente com os asserts:
"""
from abc import ABC, abstractmethod


class Visual:
    @abstractmethod
    def drawLine(self, x1, y1, x2, y2):
        pass

    @abstractmethod
    def drawRectangle(self, x, y, altura, largura):
        pass

    @abstractmethod
    def drawCircle(self, x, y, raio):
        pass


class ObjetoGeometrico:
    def __init__(self, visual):
        self.visual = visual

    def draw(self):
        pass


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Linha(ObjetoGeometrico):
    def __init__(self, visual, ponto1, ponto2):
        super().__init__(visual)
        self.ponto1 = ponto1
        self.ponto2 = ponto2

    def draw(self):
        self.visual.drawLine(self.ponto1.x, self.ponto1.y, self.ponto2.x, self.ponto2.y)


class Retangulo(ObjetoGeometrico):
    def __init__(self, visual, canto_sup_esquerdo, altura, largura):
        super().__init__(visual)
        self.canto_sup_esquerdo = canto_sup_esquerdo
        self.altura = altura
        self.largura = largura

    def draw(self):
        self.visual.drawRectangle(self.canto_sup_esquerdo.x, self.canto_sup_esquerdo.y, self.altura, self.largura)


class Circulo(ObjetoGeometrico):
    def __init__(self, visual, centro, raio):
        super().__init__(visual)
        self.centro = centro
        self.raio = raio

    def draw(self):
        self.visual.drawCircle(self.centro.x, self.centro.y, self.raio)


class ObjetoComposto(ObjetoGeometrico):
    def __init__(self, visual):
        super().__init__(visual)
        self.objetos = []

    def adicionar_objeto(self, objeto):
        self.objetos.append(objeto)

    def draw(self):
        for objeto in self.objetos:
            objeto.draw()


class FabricaObjetos:
    def __init__(self, visual):
        self.visual = visual

    def criar_linha(self, x1, y1, x2, y2):
        return Linha(self.visual, Ponto(x1, y1), Ponto(x2, y2))

    def criar_retangulo(self, x, y, altura, largura):
        return Retangulo(self.visual, Ponto(x, y), altura, largura)

    def criar_circulo(self, x, y, raio):
        return Circulo(self.visual, Ponto(x, y), raio)

    def criar_objeto_composto(self):
        return ObjetoComposto(self.visual)


# Testes
class MockVisual(Visual):
    def drawLine(self, x1, y1, x2, y2):
        assert isinstance(x1, (int, float))
        assert isinstance(y1, (int, float))
        assert isinstance(x2, (int, float))
        assert isinstance(y2, (int, float))
        print(f"Desenhando linha de ({x1}, {y1}) até ({x2}, {y2})")

    def drawRectangle(self, x, y, altura, largura):
        assert isinstance(x, (int, float))
        assert isinstance(y, (int,
