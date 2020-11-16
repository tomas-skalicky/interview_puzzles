# Task:
#
# Given a list of points, an interger k, and a point p, find the k closest points to p.
#
# Here's an example and some starter code:
#
# class Point:
#   def __init__(self, x=0, y=0):
#     self.x = x
#     self.y = y
#
#   def __repr__(self):
#     return f"({self.x}, {self.y})"
#
# def closest_points(points, k, p):
#   # Fill this in.
#
# points = [
#     Point(0, 0),
#     Point(1, 1),
#     Point(2, 2),
#     Point(3, 3),
# ]
# print(closest_points(points, 2, Point(0, 2)))
# # [(0, 0), (1, 1)]
from math import sqrt
from typing import Dict, List


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def find_closest_points(points: List[Point], k: int, p: Point) -> List[Point]:
    point_count: int = len(points)
    if point_count < k:
        raise RuntimeError('k [{}] is larger than the number of given points [{}]'.format(k, point_count))
    elif point_count == k:
        return points
    else:
        points_by_distances: Dict[float, List[Point]] = {}
        for current_point in points:
            distance = sqrt(abs(p.x - current_point.x) ** 2 + abs(p.y - current_point.y) ** 2)
            if points_by_distances.__contains__(distance):
                points_by_distances[distance].append(current_point)
            else:
                points_by_distances[distance] = [current_point]
        sorted_distances: List[float] = sorted(points_by_distances.keys())

        closest_points: List[Point] = []
        for current_distance in sorted_distances:
            current_points: List[Point] = points_by_distances[current_distance]
            current_point_size: int = len(current_points)
            remaining_number: int = k - len(closest_points)
            subset_size: int = current_point_size if remaining_number >= current_point_size else remaining_number
            closest_points = closest_points + current_points[0:subset_size]
            if len(closest_points) == k:
                return closest_points
        raise RuntimeError("Unreachable code")


points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
]
print(find_closest_points(points, 2, Point(0, 2)))
# [(1, 1), (0, 0)]
print(find_closest_points(points, 3, Point(0, 2)))
# [(1, 1), (0, 0), (2, 2)]
print(find_closest_points(points, 4, Point(0, 2)))
# [(0, 0), (1, 1), (2, 2), (3, 3)]
print(find_closest_points(points, 5, Point(0, 2)))
# RuntimeError: k [2] is larger than the number of given points [4]
