""" Using pytest for testing code """

from unittest.mock import patch
import sys
from io import StringIO
import pytest
from my_package.List_2 import *

# Funções de auxílio

run_only_success = True

def mock_user_input(monkeypatch, user_string):
    """ Mocks an user's input """
    monkeypatch.setattr('builtins.input', lambda _: f'{user_string}')

# """ 1. Faça um programa que então leia uma string e a imprima """


# """ Test Cases
#     Testar se enviar parâmetros causa erro
#     Testar se não há output
#     Que outro teste eu poderia executar para testar uma entrada do usuário feita internamente?
#     Algo que não seja string deveria dar erro?
# """

@patch('builtins.input', return_value='abcde')
def test_q1_a_input_str_print_with_str(mock_input): # Funciona
    """ ... """
    out = StringIO()
    sys.stdout = out

    q1_a_input_str_print()

    output_a = out.getvalue()
    output_b = output_a.strip()
    assert output_b == 'abcdef', str(output_a) + str(output_b)

@patch('builtins.input', return_value=None)
def test_q1_a_input_str_print_with_None(mock_input): # Funciona
    """ ... """
    out = StringIO()
    sys.stdout = out

    q1_a_input_str_print()

    output = out.getvalue().strip()
    assert output == 'None'


def test_q1_b_param_str_print(): # Funciona
    """ ... """
    str_param = 'abcde'
    
    out = StringIO()
    sys.stdout = out
    
    q1_b_param_str_print(str_param)
    
    output = out.getvalue().strip()
    assert output == str_param
