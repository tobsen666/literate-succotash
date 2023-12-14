# test_addition.py
import ctypes
import os
import pytest

# Load the C library
lib_path = os.path.join(os.path.dirname(__file__), 'addition.dll')  # Change to 'addition.so' on Linux
addition = ctypes.CDLL(lib_path)

def test_addition_case1():
    result = addition.addition(2, 3)
    assert result == 5, "Expected the sum of 2 and 3 to be 5"

def test_addition_case2():
    result = addition.addition(-1, 5)
    assert result == 3, "Expected the sum of -1 and 5 to be 3"

