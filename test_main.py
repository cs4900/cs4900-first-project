from main import *
from closest_points import find_closest_points
from convex__hull import find_convex_hull

def test_first():
    assert first == 1

def closest_points_test():
    points = [(0,0), (1,0), (1,1), (5,6), (6,9)]
    assert find_closest_points(points) == [(1, 1), (1, 0)]

def convex_hull_test():
    points = [(0,3), (2,2), (1,1), (2,1), (3,0), (0,0), (3,3)]
    assert find_convex_hull(points) == [[0,3], [0,0], [3,0], [3,3]]


