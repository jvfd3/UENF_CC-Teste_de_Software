'''

7. Escreva uma classe que represente um país. Um país é representado através dos atributos: código ISO 3166-1 (ex.: BRA), nome (ex.: Brasil), população (ex.: 193946886) e a sua dimensão em Km2 (ex.: 8515767,049). Além disso, cada país mantém uma lista de outros países com os quais ele faz fronteira. Escreva a classe em sua linguagem favorita e forneça os seus membros a seguir:
   a. Construtor que inicialize o código ISO, o nome e a dimensão do país;
   b. Métodos de acesso (getter/setter) para as propriedades código ISO, nome, população e dimensão do país;
   c. Um método que permita verificar se dois objetos representam o mesmo país (igualdade semântica. Dois países são iguais se tiverem o mesmo código ISO;
   d. Um método que informe se outro país é limítrofe do país que recebeu a mensagem;
   e. Um método que retorne a densidade populacional do país;
   f. Um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países. Considere que um país tem no máximo 40 outros países com os quais ele faz fronteira.


'''
class Pais:
    def __init__(self, codigo_iso: str, nome: str, populacao: int, dimensao: float):
        self._codigo_iso = codigo_iso
        self._nome = nome
        self._populacao = populacao
        self._dimensao = dimensao
        self._fronteiras = []
        
    def getCodigoISO(self) -> str:
        return self._codigo_iso
    
    def setCodigoISO(self, codigo_iso: str):
        self._codigo_iso = codigo_iso
    
    def getNome(self) -> str:
        return self._nome
    
    def setNome(self, nome: str):
        self._nome = nome
    
    def getPopulacao(self) -> int:
        return self._populacao
    
    def setPopulacao(self, populacao: int):
        self._populacao = populacao
    
    def getDimensao(self) -> float:
        return self._dimensao
    
    def setDimensao(self, dimensao: float):
        self._dimensao = dimensao
    
    def getFronteiras(self) -> list:
        return self._fronteiras
    
    def setFronteiras(self, fronteiras: list):
        self._fronteiras = fronteiras
    
    def mesmoPais(self, outro_pais) -> bool:
        return self.getCodigoISO() == outro_pais.getCodigoISO()
    
    def limTrofeu(self, outro_pais) -> bool:
        return outro_pais in self.getFronteiras()
    
    def densidadePopulacional(self) -> float:
        return self.getPopulacao() / self.getDimensao()
    
    def vizinhosComuns(self, outro_pais) -> list:
        return list(set(self.getFronteiras()) & set(outro_pais.getFronteiras()))

"""
Aqui, a classe País possui um construtor que inicializa o código ISO, o nome, a população e a dimensão do país. Além disso, a classe mantém uma lista de fronteiras, que é uma lista de objetos País.

A classe também possui métodos getters e setters para as propriedades código ISO, nome, população e dimensão do país.

O método mesmoPais verifica se dois objetos representam o mesmo país, comparando seus códigos ISO.

O método limTrofeu verifica se um outro país é limítrofe do país que recebeu a mensagem, verificando se o país está na lista de fronteiras do país.

O método densidadePopulacional retorna a densidade populacional do país, que é obtida pela divisão da população pela dimensão do país.

O método vizinhosComuns recebe um país como parâmetro e retorna a lista de vizinhos comuns aos dois países, ou seja, a lista de países que são fronteira dos dois países.
"""
