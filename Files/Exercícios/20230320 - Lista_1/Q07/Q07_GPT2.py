'''

7. Escreva uma classe que represente um país. Um país é representado através dos atributos: código ISO 3166-1 (ex.: BRA), nome (ex.: Brasil), população (ex.: 193946886) e a sua dimensão em Km2 (ex.: 8515767,049). Além disso, cada país mantém uma lista de outros países com os quais ele faz fronteira. Escreva a classe em sua linguagem favorita e forneça os seus membros a seguir:
   a. Construtor que inicialize o código ISO, o nome e a dimensão do país;
   b. Métodos de acesso (getter/setter) para as propriedades código ISO, nome, população e dimensão do país;
   c. Um método que permita verificar se dois objetos representam o mesmo país (igualdade semântica. Dois países são iguais se tiverem o mesmo código ISO;
   d. Um método que informe se outro país é limítrofe do país que recebeu a mensagem;
   e. Um método que retorne a densidade populacional do país;
   f. Um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países. Considere que um país tem no máximo 40 outros países com os quais ele faz fronteira.


'''

"""
João Vítor Fernandes Dias
Mais uma vez você se esqueceu de utilizar o assert. Reescreva seu código utilizando o assert para realizar os testes.

Desculpe pelo erro. Aqui está o código atualizado com o uso de assert para testes:
"""

class Country:
    def __init__(self, iso, name, population, area):
        self._iso = iso
        self._name = name
        self._population = population
        self._area = area
        self._neighbors = []

    def get_iso(self):
        return self._iso

    def set_iso(self, iso):
        self._iso = iso

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_population(self):
        return self._population

    def set_population(self, population):
        self._population = population

    def get_area(self):
        return self._area

    def set_area(self, area):
        self._area = area

    def is_same_country(self, other):
        return self._iso == other.get_iso()

    def is_neighbor(self, other):
        return other in self._neighbors

    def get_population_density(self):
        return self._population / self._area

    def get_common_neighbors(self, other):
        return list(set(self._neighbors).intersection(set(other._neighbors)))

# testes
brasil = Country('BRA', 'Brasil', 211000000, 8515767)
argentina = Country('ARG', 'Argentina', 44940000, 2780400)
bolivia = Country('BOL', 'Bolívia', 11310000, 1098581)
paraguai = Country('PRY', 'Paraguai', 7153000, 406752)
uruguai = Country('URY', 'Uruguai', 3462000, 176215)
brasil._neighbors = [argentina, bolivia, paraguai, uruguai]
argentina._neighbors = [brasil, bolivia, uruguai]
bolivia._neighbors = [brasil, argentina, paraguai]
paraguai._neighbors = [brasil, bolivia]
uruguai._neighbors = [brasil, argentina]

assert brasil.get_iso() == 'BRA'
assert brasil.get_name() == 'Brasil'
assert brasil.get_population() == 211000000
assert brasil.get_area() == 8515767
assert argentina.is_same_country(brasil) == False
assert argentina.is_same_country(argentina) == True
assert bolivia.is_neighbor(brasil) == True
assert paraguai.is_neighbor(uruguai) == False
assert brasil.get_population_density() == 24.74414241192314
assert brasil.get_common_neighbors(argentina) == [uruguai, bolivia]
assert uruguai.get_common_neighbors(paraguai) == []
