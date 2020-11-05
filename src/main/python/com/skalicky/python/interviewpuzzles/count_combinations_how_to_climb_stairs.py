# Task:
#
# You are given a positive integer N which represents the number of steps in a staircase. You can either climb
# 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
#
# def staircase(n):
#   # Fill this in.
#
# print staircase(4)
# # 5
# print staircase(5)
# # 8
#
# Can you find a solution in O(n) time?
from math import factorial, floor


def staircase_fibonacchi(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        fibn_minus_1: int = 1
        fibn: int = 2
        for i in range(3, n + 1):
            fibn_minus_2: int = fibn_minus_1
            fibn_minus_1: int = fibn
            fibn: int = fibn_minus_1 + fibn_minus_2
        return fibn


def staircase_combinatorics(n: int) -> int:
    total_count: int = 0
    for two_count in range(0, floor(n / 2) + 1):
        items_to_permutate: int = n - two_count
        total_count = total_count + floor(
            factorial(items_to_permutate) / (factorial(items_to_permutate - two_count) * factorial(two_count)))
    return total_count


print(staircase_fibonacchi(4))
# 5
print(staircase_combinatorics(4))
# 5
print(staircase_fibonacchi(1))
# 1
print(staircase_combinatorics(1))
# 1
print(staircase_fibonacchi(2))
# 2
print(staircase_combinatorics(2))
# 2
print(staircase_fibonacchi(5))
# 8
print(staircase_combinatorics(5))
# 8

# Fibonacci sequence:
# - proved by a mathematical induction
#   (1) The statement stands for n=1.
#   (2) Assuming the statement stands for n -> the last column contains Fib(n-1) ones and Fib(n-2) twos.
#       We add a new column with only ones and get Fib(n) rows ending with ones.
#       We take rows ending with twice ones (from the assumption Fib(n-1), copy them and replace these twice ones with
#       twos.
#
# n=1
# 1
#
# n=2
# 1 1
# 2 .
#
# n=3
# 1 1 1
# 2 . 1
# 1 2 .
#
# n=4
# 1 1 1 1
# 2 . 1 1
# 1 2 . 1
# 1 1 2 .
# 2 . 2 .
#
# n=5
# 1 1 1 1 1
# 2 . 1 1 1
# 1 2 . 1 1
# 1 1 2 . 1
# 2 . 2 . 1
# 1 1 1 2 .
# 2 . 1 2 .
# 1 2 . 2 .
#
# n=6
# 1 1 1 1 1 1
# 2 . 1 1 1 1
# 1 2 . 1 1 1
# 1 1 2 . 1 1
# 1 1 1 2 . 1
# 2 . 1 2 . 1
# 1 2 . 2 . 1
# 2 . 2 . 1 1
# 1 1 1 1 2 .
# 2 . 1 1 2 .
# 1 2 . 1 2 .
# 1 1 2 . 2 .
# 2 . 2 . 2 .
