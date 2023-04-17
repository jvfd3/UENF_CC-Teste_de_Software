'''

1. Identifique as classes e implemente um programa para a seguinte especificacao: “O supermercado vende diferentes tipos de produtos. Cada produto tem um preco e uma quantidade em estoque. Um pedido de um cliente e composto de itens, onde cada item especifica o produto que o cliente deseja e a respectiva quantidade. Esse pedido pode ser pago em dinheiro, cheque ou cartão.”

'''

"""
Para a especificação apresentada, é possível identificar as seguintes classes:

Produto: responsável por armazenar as informações sobre cada tipo de produto, como preço e quantidade em estoque.
Item: representa um item de um pedido, especificando o produto e a quantidade desejada pelo cliente.
Pedido: contém a lista de itens que um cliente deseja comprar e o método de pagamento escolhido.
Pagamento: representa uma forma de pagamento, podendo ser dinheiro, cheque ou cartão.
Segue abaixo uma possível implementação dessas classes em Python, com comentários explicando as partes relevantes do código:
"""

class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def atualizar_estoque(self, quantidade: int):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            return True
        else:
            return False

class Item:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_valor(self):
        return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self, itens: list, forma_pagamento: str):
        self.itens = itens
        self.forma_pagamento = forma_pagamento

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item.calcular_valor()
        return total

    def processar_pedido(self):
        for item in self.itens:
            if not item.produto.atualizar_estoque(item.quantidade):
                return False
        return True

class Pagamento:
    def __init__(self, valor: float, forma: str):
        self.valor = valor
        self.forma = forma

    def processar_pagamento(self):
        # lógica de processamento de pagamento (não implementada neste exemplo)
        pass

# Para testar o funcionamento das classes acima, pode-se criar objetos de exemplo e executar algumas operações. Por exemplo:

# João Vítor Fernandes Dias
# Reescreva apenas o código que testa o funcionamento e faça com que ele utilize da função "assert" para averiguar o adequado funcionamento das classes.

# Claro! Segue abaixo o código que testa o funcionamento das classes, utilizando a função assert para verificar o correto funcionamento:

# criar alguns produtos
p1 = Produto("Arroz", 10.0, 20)
p2 = Produto("Feijão", 8.0, 15)
p3 = Produto("Macarrão", 5.0, 30)

# criar alguns itens
i1 = Item(p1, 2)
i2 = Item(p2, 3)
i3 = Item(p3, 4)

# criar um pedido com os itens acima e forma de pagamento em dinheiro
pedido = Pedido([i1, i2, i3], "dinheiro")

# calcular o total do pedido
total = pedido.calcular_total()
assert total == 62.0, f"Total incorreto: {total}"

# processar o pedido (atualizando o estoque dos produtos)
sucesso = pedido.processar_pedido()
assert sucesso, "Não foi possível processar o pedido."

# tentar processar o pedido novamente (deve falhar porque não há estoque suficiente)
sucesso = pedido.processar_pedido()
assert not sucesso, "Pedido processado indevidamente."

# realizar um pagamento (não há implementação para o processamento de pagamento neste exemplo)
pagamento = Pagamento(total, "dinheiro")
pagamento.processar_pagamento()

# Neste código, a função assert é utilizada para verificar se os resultados obtidos estão corretos. Se algum dos testes falhar, uma exceção AssertionError será lançada, indicando que há um problema com a implementação.




