# import sympy and Point, Line  
import math  

def find_closest_points(points):

    distance_map = {}

    for i in range(len(points)):
        for j in range(len(points)):
            if i==j:
                continue
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[j][0], points[j][1]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            distance_map[distance] = [points[i], points[j]]

    min_distance = float('inf')
    for key, val in distance_map.items():
        min_distance = min(min_distance, key)

    return distance_map[min_distance]

find_closest_points()
        
