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


# Questão 2

def test_q2(): # Success
    """ ... """
    # if run_only_success:
    #     return

    str_param = 'abcde'
    size = str(len(str_param))

    out = StringIO()
    sys.stdout = out

    q2_(str_param)

    output = out.getvalue().strip()
    condition = output == size
    error_message = 'Error: '
    error_message += output + '==' + size
    error_message += '\t'+str(type(output)) + '==' + str(type(size))

    assert condition, error_message
