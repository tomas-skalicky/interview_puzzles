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


def staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        fibn_minus_1 = 1
        fibn = 2
        for i in range(3, n + 1):
            fibn_minus_2 = fibn_minus_1
            fibn_minus_1 = fibn
            fibn = fibn_minus_1 + fibn_minus_2
        return fibn


print(staircase(4))
# 5
print(staircase(1))
# 1
print(staircase(2))
# 2
print(staircase(5))
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
