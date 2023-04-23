""" Using pytest for testing code """

# from unittest.mock import patch
import sys
from io import StringIO
# import pytest
from my_package.List_2 import *

# Funções de auxílio

run_only_success = True

def mock_user_input(monkeypatch, user_string):
    """ Mocks an user's input """
    monkeypatch.setattr('builtins.input', lambda _: f'{user_string}')

# """
# 8. Faça um programa que contenha um menu com as seguintes opções:

#   1. Ler uma string S1 (tamanho máximo 20 caracteres)
#   2. Imprimir o tamanho da string S1
#   3. Comparar a string S1 com uma nova string S2 fornecida pelo usuário e imprimir o resultado da comparação
#   4. Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da concatenação
#   5. Imprimir a string S1 de forma reversa
#   6. Contar quantas vezes um dado caractere aparece na string S1. Esse caractere desse ser informado pelo usuário
#   7. Substituir a primeira ocorrêcia do caractere C1 da string S1 pelo caractere C2. Os caracteres C1 e C2 serão lidos pelo usuário
#   8. Verificar se uma string S2 é substring de S1. A string S2 deve ser informada pelo usuário
#   9. Retornar uma substring da string S1. Para isso o usuário deve informar a partir de qual posição deve ser criada a substring e qual é o tamanho da substring.
# """


def test_q8_1_input_19_char(monkeypatch): # OK
    """ 1. Ler uma string S1 (tamanho máximo 20 caracteres) """
    test_q8_read_string_instance = q8()
    test_input = 19*'.' # uma string de até 20 caracteres (19)
    mock_user_input(monkeypatch, test_input) # Simula o input do usuário
    test_q8_read_string_instance.read_string() # teste a leitura
    
    output = test_q8_read_string_instance.S1
    expected_output = test_input
    error_message = 'O valor de entrada deveria ter sido ' + '"'+expected_output+'".'
    assert output == expected_output, error_message

def test_q8_1_input_20_char(monkeypatch): # OK
    """ 1. Ler uma string S1 (tamanho máximo 20 caracteres) """
    test_q8_read_string_instance = q8()
    test_input = 20*'.' # uma string de 20 caracteres
    mock_user_input(monkeypatch, test_input) # Simula o input do usuário
    test_q8_read_string_instance.read_string() # teste a leitura
    
    output = test_q8_read_string_instance.S1
    expected_output = test_input
    error_message = 'O valor de entrada deveria ter sido ' + '"'+expected_output+'".'
    assert output == expected_output, error_message

def test_q8_1_input_21_char(monkeypatch): # Fail
    """ 1. Ler uma string S1 (tamanho máximo 20 caracteres) """
    test_q8_read_string_instance = q8()
    test_input = 21*'.' # uma string de 20 caracteres
    mock_user_input(monkeypatch, test_input) # Simula o input do usuário
    test_q8_read_string_instance.read_string() # teste a leitura
    
    output = test_q8_read_string_instance.S1
    expected_output = ''
    error_message = 'O valor de entrada deveria ter sido ' + '"'+expected_output+'".'
    # joaoluiz.af@gmail.com
    assert output == expected_output, error_message
