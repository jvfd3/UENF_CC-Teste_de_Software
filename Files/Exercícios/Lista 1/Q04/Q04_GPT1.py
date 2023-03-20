'''

4. Escreva o programa Contador, que encapsule um valor usado para contagem de itens ou eventos. A classe deve oferecer métodos que devem:
   a. Zerar;
   b. Incrementar;
   c. Retornar o valor do contador.

'''

class Contador:
    def __init__(self):
        self.valor = 0
        
    def zerar(self):
        self.valor = 0
        
    def incrementar(self):
        self.valor += 1
        
    def obter_valor(self):
        return self.valor


# testando a classe
c = Contador()
assert c.obter_valor() == 0

c.incrementar()
assert c.obter_valor() == 1

c.incrementar()
assert c.obter_valor() == 2

c.zerar()
assert c.obter_valor() == 0

"""
Neste código, criamos a classe Contador que encapsula um valor usado para contagem de itens ou eventos. O construtor inicializa o valor com zero. A classe oferece três métodos:

zerar: que redefine o valor do contador para zero.
incrementar: que incrementa em uma unidade o valor do contador.
obter_valor: que retorna o valor atual do contador.
Em seguida, utilizamos o assert para testar a classe e verificar se a implementação está correta. Verificamos o valor inicial, incrementamos o contador duas vezes, zeramos o contador e verificamos se o valor final é zero.
"""
