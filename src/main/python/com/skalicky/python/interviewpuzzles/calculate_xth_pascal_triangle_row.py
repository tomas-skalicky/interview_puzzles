# Task:
#
# Pascal's Triangle is a triangle where all numbers are the sum of the two numbers above it. Here's an example of
# the Pascal's Triangle of size 5.
#
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
#
# Given an integer n, generate the n-th row of the Pascal's Triangle.
#
# Here's an example and some starter code.
#
# def pascal_triangle_row(n):
#   # Fill this in.
#
# print(pascal_triangle_row(6))
# # [1, 5, 10, 10, 5, 1]
from typing import List


def calculate_xth_pascal_triangle_row(x: int) -> List[int]:
    """Time complexity ... O(x ^ 2) because the number of numbers in the triangle is not greater than
     (x+1) * ((x+1)+1) / 2 where (x+1) is the number of rows and number of numbers in the last row, 1 is for
     the number of numbers in the first row and ((x+1)+1) / 2 is the average of numbers in rows.
    """

    current_row: List[int] = [0, 1, 0]
    current_row_number: int = 0
    while current_row_number < x:
        new_row: List[int] = [0]
        for i in range(0, len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])
        new_row.append(0)
        current_row = new_row
        current_row_number += 1
    return current_row[1:len(current_row) - 1]
