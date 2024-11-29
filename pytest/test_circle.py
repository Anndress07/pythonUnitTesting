import pytest
import source.shapes as shapes
import math

class TestCircle:
    # executes once for each test
    def setup_method(self, method):
        print(f"Setting Up {method}")
        self.circle = shapes.Circle(10)

    # executes once for each test
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_radius(self):
        assert self.circle.area() == math.pi*self.circle.radius**2

    def test_perimiter(self):
        result = self.circle.perimeter()
        expected = 2*math.pi*self.circle.radius

        assert result == expected

    # def test_tw
    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()


