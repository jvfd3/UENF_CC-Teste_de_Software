'''

2. Faca um programa para controle de emprestimo de livros, com as classes Emprestimo, Livro e Pessoa.

'''

"""
Neste código você novamente não utilizou o assert, nem comentou as partes relevantes do código. Por favor, reescreva seu código.

Desculpe pelo erro anterior. Aqui está a reescrita do código utilizando a função assert para testar o funcionamento das classes:
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
            emprestimo = Emprestimo(self, pessoa, data_emprestimo)
            pessoa.emprestimos.append(emprestimo)
            return True


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

    def realizar_emprestimo(self, livro, data_emprestimo):
        emprestimo = livro.emprestar(self, data_emprestimo)
        assert emprestimo is not False, "Livro não está disponível para empréstimo."
        self.emprestimos.append(emprestimo)
        assert emprestimo in self.emprestimos, "Empréstimo não foi registrado na lista de empréstimos da pessoa."
        return emprestimo


# Testando o código
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis")
pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

# Verificando se o empréstimo de um livro funciona corretamente
emprestimo1 = pessoa1.realizar_emprestimo(livro1, "20/03/2023")
assert emprestimo1.livro == livro1, "Livro emprestado não é o esperado."
assert emprestimo1.pessoa == pessoa1, "Pessoa que fez o empréstimo não é a esperada."
assert emprestimo1.data_emprestimo == "20/03/2023", "Data de empréstimo não é a esperada."
assert livro1.disponivel == False, "Livro deveria estar indisponível após empréstimo."
assert emprestimo1 in pessoa1.emprestimos, "Empréstimo não foi registrado na lista de empréstimos da pessoa."

# Verificando se não é possível emprestar um livro que não está disponível
livro2.disponivel = False
emprestimo2 = pessoa2.realizar_emprestimo(livro2, "20/03/2023")
assert emprestimo2 is False, "Livro indisponível foi emprestado."

# Verificando se a devolução de um livro funciona corretamente
emprestimo1.devolver("25/03/2023")
assert emprestimo1.data_devolucao == "25/03/2023", "Data de devolução
