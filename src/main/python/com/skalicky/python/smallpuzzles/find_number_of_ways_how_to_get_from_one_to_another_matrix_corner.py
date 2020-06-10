# Task:
#
# You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to
# the bottom-right of the matrix y going only right or down.
#
# Example:
# n = 2, m = 2
#
# This should return 2, since the only possible routes are:
# Right, down
# Down, right.
#
# Here's the signature:
#
# def num_ways(n, m):
#   # Fill this in.
#
# print num_ways(2, 2)
# # 2
from math import factorial, floor


def num_ways(n: int, m: int):
    return floor(factorial(n - 1 + m - 1) / factorial(n - 1) / factorial(m - 1))


print(num_ways(2, 2))
# 2
print(num_ways(3, 4))
# 10

# The problem is a problem of permutations with repetition.
# 2x2 (1x1)
# _ |     1+1 = 2*1 / (1 * 1)
# | _

# 3x2 (2x1)
# _ _ |   2+1 = 3*2*1 / (2*1 * 1)
# _ | _
# | _ _

# 3x3 (2x2)
# _ _ | |   3+2+1 = 4*3*2*1 / (2*1 * 2*1)
# _ | _ |
# | _ _ |
# _ | | _
# | _ | _
# | | _ _

# 4x3 (3x2)
# _ _ _ | |   4+3+2+1 = 5*4*3*2*1 / (3*2*1 * 2*1)
# _ _ | _ |
# _ | _ _ |
# | _ _ _ |
# _ _ | | _
# _ | _ | _
# | _ _ | _
# _ | | _ _
# | _ | _ _
# | | _ _ _
