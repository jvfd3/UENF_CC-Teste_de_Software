'''

2. Faca um programa para controle de emprestimo de livros, com as classes Emprestimo, Livro e Pessoa.

'''

"""
Agora uma nova questão:

2. Faca um programa para controle de emprestimo de livros, com as classes Emprestimo, Livro e Pessoa.

Claro! Segue abaixo a implementação das classes Emprestimo, Livro e Pessoa, que compõem o sistema de controle de empréstimo de livros:
"""

class Emprestimo:
    def __init__(self, livro, pessoa, data_emprestimo):
        self.livro = livro
        self.pessoa = pessoa
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None

    def devolver(self, data_devolucao):
        self.data_devolucao = data_devolucao
        self.livro.disponivel = True


class Livro:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self, pessoa, data_emprestimo):
        if not self.disponivel:
            return False
        else:
            self.disponivel = False
            Emprestimo(self, pessoa, data_emprestimo)
            return True


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

    def realizar_emprestimo(self, livro, data_emprestimo):
        emprestimo = livro.emprestar(self, data_emprestimo)
        if emprestimo:
            self.emprestimos.append(emprestimo)
        return emprestimo


"""
A classe Emprestimo representa um empréstimo de um livro para uma pessoa, e guarda informações sobre o livro emprestado, a pessoa que fez o empréstimo, a data do empréstimo e a data prevista para devolução. A data de devolução é armazenada quando o livro é devolvido através do método devolver.

A classe Livro representa um livro, e guarda informações sobre seu título, autor e disponibilidade. O método emprestar é utilizado para emprestar o livro para uma pessoa, criando um novo objeto Emprestimo e marcando o livro como indisponível.

A classe Pessoa representa uma pessoa que pode realizar empréstimos de livros. O método realizar_emprestimo é utilizado para realizar um novo empréstimo de um livro, chamando o método emprestar da classe Livro e adicionando o empréstimo na lista de empréstimos da pessoa.
"""