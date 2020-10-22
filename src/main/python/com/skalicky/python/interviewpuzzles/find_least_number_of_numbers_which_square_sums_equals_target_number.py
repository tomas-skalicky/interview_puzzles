# Task:
#
# Given a number n, find the least number of squares needed to sum up to the number.
#
# Here's an example and some starting code:
#
# def square_sum(n):
#   # Fill this in.
#
# print(square_sum(13))
# # Min sum is 32 + 22
# # 2
from math import sqrt, floor


def square_sum(n: int) -> int:
    rest: int = n
    count: int = 0
    while rest != 0:
        rest = rest - floor(sqrt(rest)) ** 2
        count += 1
    return count
