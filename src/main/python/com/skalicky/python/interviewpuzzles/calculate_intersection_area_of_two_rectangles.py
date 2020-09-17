# Task:
#
# Given two rectangles, find the area of intersection.
#
# Here's some starter code and a starter example:
#
# class Rectangle():
#   def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
#     self.min_x = min_x
#     self.min_y = min_y
#     self.max_x = max_x
#     self.max_y = max_y
#
# def intersection_area(rect1, rect2):
#   # Fill this in.
#
# #  BBB
# # AXXB
# # AAA
# rect1 = Rectangle(0, 0, 3, 2)
# rect2 = Rectangle(1, 1, 3, 3)
#
# print(intersection_area(rect1, rect2))
# # 2


class Rectangle:
    def __init__(self, min_x=0, min_y=0, max_x_excluded=0, max_y_excluded=0):
        self.min_x: int = min_x
        self.min_y: int = min_y
        self.max_x_excluded: int = max_x_excluded
        self.max_y_excluded: int = max_y_excluded


def intersection_area(rect1: Rectangle, rect2: Rectangle):
    min_x: int = max(rect1.min_x, rect2.min_x)
    max_x_excluded: int = min(rect1.max_x_excluded, rect2.max_x_excluded)
    min_y: int = max(rect1.min_y, rect2.min_y)
    max_y_excluded: int = min(rect1.max_y_excluded, rect2.max_y_excluded)
    return (max_x_excluded - min_x) * (
                max_y_excluded - min_y) if max_x_excluded >= min_x and max_y_excluded >= min_y else 0


# 2  BB
# 1 AXX
# 0 AAA
#   012
#######
rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(1, 1, 3, 3)
print(intersection_area(rect1, rect2))
# 2

# 2    B
# 1 AAAB
# 0 AAA
#   0123
########
rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(3, 1, 4, 3)
print(intersection_area(rect1, rect2))
# 0

# 3     B
# 2     B
# 1
# 0 AAA
#   01234
#########
rect1 = Rectangle(0, 0, 3, 1)
rect2 = Rectangle(4, 2, 5, 4)
print(intersection_area(rect1, rect2))
# 0

# 1 XXX
# 0 XXX
#   012
#######
rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(0, 0, 3, 2)
print(intersection_area(rect1, rect2))
# 6
