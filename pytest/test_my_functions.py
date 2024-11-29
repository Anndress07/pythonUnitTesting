import pytest
import source.myfunctions as my_functions
import time


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5;

def test_divide():
    result = my_functions.divide(10,5)
    assert result == 2;

def test_add_strings():
    result = my_functions.add("i like ", "burgers")
    assert result=="i like burgers"

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10,0)
        """ we are expecting a valueError error when we call this function"""

"""
Only run slow tests with >> pytest -m slow
"""

@pytest.mark.slow # marks a slow test!
def test_very_slow():
    time.sleep(3)
    result = my_functions.divide(10, 5)
    assert result == 2;

@pytest.mark.skip(reason="This feature is currently broken")
def  test_add():
    my_functions.add(1, 3)

@pytest.mark.xfail(reason="cannot divide by zero")
def test_divide_broken():
    my_functions.divide(4,0)
