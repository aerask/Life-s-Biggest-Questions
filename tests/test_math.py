"""
Testing for the math.py module.
"""

import lbq as lbq #runs a test on the lbq in the same directory as tests/
import pytest

def test_add():
    #assert True #if you're testing you want asserts, if you're running you want exceptions
    assert lbq.math.add(5, 2) == 7
    assert lbq.math.add(2, 5) == 7

def test_mult():
    assert lbq.math.mult(5, 2) == 10
    assert lbq.math.mult(2, 5) == 10
