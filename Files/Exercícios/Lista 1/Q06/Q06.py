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

def main():
    ''' Main code to solve the exercise '''

main()