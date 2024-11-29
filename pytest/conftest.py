import pytest
import source.shapes as shapes

"""
Fixtures that can be accessed across multiple files. 
"""
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10,20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5,6)
