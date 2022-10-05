from main import *

def test_intersection():
    points = (sympy.Point(0,0), sympy.Point(2,2), sympy.Point(2,0), sympy.Point(0,2))
    assert calculate_intersection(points) == (1,1)