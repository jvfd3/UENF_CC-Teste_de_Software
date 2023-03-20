# Envios Teste de Software

## 20230320 - Lista de exercícios

### Descrição

> Lista de exercicios
> João Luiz de Almeida Filho
> 15 de mar.
> 100 pontos
> Data de entrega: 20 de mar.
> Turma, estou enviando em anexo uma lista de exercícios para programação OO. Ela será usada apenas para a prática de vocês sobre o tema. Deste modo, tentem utilizar boas práticas de programação OO e também de engenharia de software. NÃO É UMA LISTA DE EXERCICIOS OBRIGATÓRIA, mas recomendo fazê-la. Podemos discutir alguns exercícios dela na próxima aula
> Recomendo também utilizar o git para controle de versões destes exercícios (crie um projeto para todos os exercicios da lista e separe cada exercicio por pasta). Neste caso, criem commites a cada exercicio pronto ou cada passo na direção da solução do problema (altamente recomendado).
> Caso tenha alguem que não saiba utilizar o GIT mande uma mensagem

### Lista de exercícios

1. Identifique as classes e implemente um programa para a seguinte especificacao: “O supermercado vende diferentes tipos de produtos. Cada produto tem um preco e uma quantidade em estoque. Um pedido de um cliente e composto de itens, onde cada item especifica o produto que o cliente deseja e a respectiva quantidade. Esse pedido pode ser pago em dinheiro, cheque ou cartão.”
2. Faca um programa para controle de emprestimo de livros, com as classes Emprestimo, Livro e Pessoa.
3. Faca um programa que calcule a area de uma figura geometrica. Aceite quatro tipos de figura geometrica: quadrado, retangulo, triangulo e circulo. Use heranca e polimorfismo.
4. Escreva o programa Contador, que encapsule um valor usado para contagem de itens ou eventos. A classe deve oferecer métodos que devem:
   a. Zerar;
   b. Incrementar;
   c. Retornar o valor do contador.
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
6. Considere que uma biblioteca gráfica disponibiliza uma classe Visual os métodos da Tabela 1. A partir desta biblioteca:
   a. Escreve uma classe que seja capaz de armazenar o estado e plotar um objeto geométrico (plotar no caso seria imprimir os vértices e no caso de um círculo as coordenadas do centro e seu raio).
   b. Defina uma interface única para desenhar os objetos e crie uma classe que permita agregar objetos geométricos simples (linha, retângulo e círculo) e compostos (objetos que já agregam outros objetos). (Leia sobre o padrão de projeto composite)
   c. Escreva uma fábrica (leia sobre o padrão de projeto Factory) para construir objetos simples (um único método) e compostos (outro método).
7. Escreva uma classe que represente um país. Um país é representado através dos atributos: código ISO 3166-1 (ex.: BRA), nome (ex.: Brasil), população (ex.: 193946886) e a sua dimensão em Km2 (ex.: 8515767,049). Além disso, cada país mantém uma lista de outros países com os quais ele faz fronteira. Escreva a classe em sua linguagem favorita e forneça os seus membros a seguir:
   a. Construtor que inicialize o código ISO, o nome e a dimensão do país;
   b. Métodos de acesso (getter/setter) para as propriedades código ISO, nome, população e dimensão do país;
   c. Um método que permita verificar se dois objetos representam o mesmo país (igualdade semântica. Dois países são iguais se tiverem o mesmo código ISO;
   d. Um método que informe se outro país é limítrofe do país que recebeu a mensagem;
   e. Um método que retorne a densidade populacional do país;
   f. Um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países. Considere que um país tem no máximo 40 outros países com os quais ele faz fronteira.

#### Tabela 1

| Função | Descrição | Variáveis |
|------|-----------|---|
| drawLine(x1, y1, x2, y2) | Desenha uma linha. | x1 e y1 - coordenadas do ponto de origem; x2 e y2 - coordenadas do ponto de destino. |
| drawRectangle(x, y, altura, largura) | Desenha um retângulo. | x e y - coordenadas do canto esquerdo superior; altura e largura do retângulo. |
| drawCircle(x, y, raio) | Desenha um círculo. | x e y - coordenadas do centro; raio - raio do círculo. |

## x
