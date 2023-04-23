""" Using pytest for testing code """

# from unittest.mock import patch
import sys
from io import StringIO
# import pytest
from my_package.List_2 import *

# Funções de auxílio

# run_only_success = True

# def mock_user_input(monkeypatch, user_string):
#     """ Mocks an user's input """
#     monkeypatch.setattr('builtins.input', lambda _: f'{user_string}')


def test_q4():
    """ ... """
    error_message = ''
    condition = True
    assert condition, error_message
    
    
def test_q4_():
    """ Test Cases
        input_q4_ = 'agda'
        input_q4_ = 'Arnaldo'
        input_q4_ = 'aristides'
        input_q4_ = 'beto'
        input_q4_ = 'casé'
        input_q4_ = 10*'A'
        input_q4_ = 10*'a'
        input_q4_ = 'b'+10*'A'
        input_q4_ = 'B'+10*'a'
        input_q4_ = typeError
        Tem como testar se a função printou algo?
    """
    pass