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


# Questão 3

# """ 3. Faça um programa que conte o número de 1's que aparecem em um string. Exemplo: 0011001 -> 3 """

def test_q3_if_empty_string_returns_0():
    """ Not necessary now """
    assert q3('') == 0, "Should be 0"

def test_q3_if_000_returns_0():
    """ Not necessary now """
    assert q3(3*'0') == 0, "Should be 0"

def test_q3_if_a_returns_10():
    """ Not necessary now """
    assert q3(10*'01') == 10, "Should be 10"

def test_q3_if_b_returns_20():
    """ Not necessary now """
    assert q3(10*'11') == 20, "Should be 20"

def test_q3_if_c_returns_4():
    """ Not necessary now """
    assert q3('01n09r19uf28yg94b18721') == 4, "Should be 4"

