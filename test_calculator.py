# Import pytest or use built-in assertions
import pytest

# Assuming the calculator functions are defined in another file and imported here
# For demonstration, I'll include the functions directly in this example

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Unit tests
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(-1, 8) == 7
    assert add(4, 4) == 8
    assert add(6, 5) == 11
    assert add(9,7 ) == 16

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0
    assert subtract(8, 6) == 2
    assert subtract(5 , 4 ) == 1
    assert subtract(8, 4) == 4
    assert subtract(5 , 8 ) == -3

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(5, 1 ) == 5
    assert multiply(4,2 ) == 8
    assert multiply(5, 3 ) == 15
    assert multiply(4, -2 ) == -8


def test_divide():
    assert divide(4, 2) == 2
    assert divide(5, 2) == 2.5
    assert divide(1, 0) == "Error! Division by zero."
    assert divide(-1, -1) == 1
    assert divide(6,2 ) == 3
    assert divide(14,2 ) == 7
    assert divide(8,2 ) == 4
    
