"""
A small set of functions for doing math operations.
"""

# Write a function named add that adds two values


def add(a, b):
    """
    Addition between two arguments
    a: float
    E = sum_ x y z
    """
    return a + b


def mult(a, b):
    """
    Multiplication between two arguments
    """
    return a * b


def greater(a, b):
    """
    Check for greater between two arguments
    """
    if a >= b:
        return a
    elif a < b:
        return b
    else:
        print('Something weird happened')
        return 0
