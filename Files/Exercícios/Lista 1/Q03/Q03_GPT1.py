'''

3. Faca um programa que calcule a area de uma figura geometrica. Aceite quatro tipos de figura geometrica: quadrado, retangulo, triangulo e circulo. Use heranca e polimorfismo.

'''

"""
Agora um novo código. Peço que atente para o uso do assert para a testagem do código e também utilize os comentários para explicar a lógica do código até mesmo durante a definição das classes.

3. Faca um programa que calcule a area de uma figura geometrica. Aceite quatro tipos de figura geometrica: quadrado, retangulo, triangulo e circulo. Use heranca e polimorfismo.
"""

class FiguraGeometrica:
    def calcular_area(self):
        pass
    
class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return self.lado ** 2
    
class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
    
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
        return 3.14159 * (self.raio ** 2)


# testando as classes
q = Quadrado(5)
assert q.calcular_area() == 25

r = Retangulo(4, 6)
assert r.calcular_area() == 24

t = Triangulo(3, 8)
assert t.calcular_area() == 12

c = Circulo(2)
assert c.calcular_area() == 12.56636

"""
Neste código, criamos uma classe base FiguraGeometrica que possui um método calcular_area que deve ser sobrescrito pelas subclasses. A partir disso, criamos quatro subclasses, cada uma correspondendo a uma figura geométrica: Quadrado, Retangulo, Triangulo e Circulo. Cada uma delas recebe os parâmetros necessários em seu construtor e implementa o método calcular_area de acordo com a fórmula correspondente.

Em seguida, utilizamos o assert para testar as classes e verificar se a implementação está correta. Os resultados esperados foram calculados previamente e comparados com o resultado retornado pela chamada do método calcular_area para cada objeto.
"""
