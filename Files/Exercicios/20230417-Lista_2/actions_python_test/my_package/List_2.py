""" Lista 2 """

def q1_a_input_str_print():
    """ 1. Faça um programa que então leia uma string e a imprima """
    print(input())

def q1_b_param_str_print(str_param):
    """ 1. Faça um programa que então leia uma string e a imprima """
    print(str_param)


def q2_(str_param):
    """ 2. Crie um programa que imprima o comprimento de uma string """
    print(len(str_param))

def q3_(str_param):
    """ 3. Faça um programa que conte o número de 1's que aparecem em um string. Exemplo: 0011001 -> 3 """
    return str_param.count('1')

""" 4. Entre com um nome e imprima o nome somente se a primeira letra do nome for "a" (maiúscula ou minúscula) """

def q4_(str_param):
    if str_param[0] in ['a', 'A']:
        print(srt_param)


# class q8():
#     """ 8. Faça um programa que contenha um menu com as seguintes opções:
#         1. Ler uma string S1 (tamanho máximo 20 caracteres)
#         2. Imprimir o tamanho da string S1
#         3. Comparar a string S1 com uma nova string S2 fornecida pelo usuário e imprimir o resultado da comparação
#         4. Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da concatenação
#         5. Imprimir a string S1 de forma reversa
#         6. Contar quantas vezes um dado caractere aparece na string S1. Esse caractere desse ser informado pelo usuário
#         7. Substituir a primeira ocorrêcia do caractere C1 da string S1 pelo caractere C2. Os caracteres C1 e C2 serão lidos pelo usuário
#         8. Verificar se uma string S2 é substring de S1. A string S2 deve ser informada pelo usuário
#         9. Retornar uma substring da string S1. Para isso o usuário deve informar a partir de qual posição deve ser criada a substring e qual é o tamanho da substring.
#     """
#     def __init__(self):
#         """ construtor """

#     def read_string(self):
#         """ reads string """
    
#     def S1_size(self):
#         """ gets S1 size """

