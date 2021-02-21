import pytest
#This is your function
def multiply(a ,b):
    c = a * b
    return c
def addition(a ,b):
    c = a + b + b
    return c

#This is your test
def test_multiply():
    a1 = 10
    b1 = 12
    assert multiply(a1, b1) == 120
def test_addition():
    a1 = 112
    b1 = 123
    assert addition(a1, b1) == 235