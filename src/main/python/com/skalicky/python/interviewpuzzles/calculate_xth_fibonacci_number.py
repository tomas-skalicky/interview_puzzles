# Task:
#
# The Fibonacci sequence is the integer sequence defined by the recurrence relation: F(n) = F(n-1) + F(n-2), where
# F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci number is the sum of the prior two Fibonacci numbers. Below
# are the first few values of the sequence:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
#
# Given a number n, print the n-th Fibonacci Number.
# Examples:
# Input: n = 3
# Output: 2
#
# Input: n = 7
# Output: 13
# Here's a starting point:
#
# class Solution():
#   def fibonacci(self, n):
#     # fill this in.
#
# n = 9
# print(Solution().fibonacci(n))
# # 34


class Solution:
    @staticmethod
    def fibonacci(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_number_minus_1: int = 0
            fib_number: int = 1
            for i in range(2, n + 1):
                current_fib_number: int = fib_number_minus_1 + fib_number
                fib_number_minus_1 = fib_number
                fib_number = current_fib_number
            return fib_number


print(Solution.fibonacci(0))
# 0
print(Solution.fibonacci(1))
# 1
print(Solution.fibonacci(2))
# 1
print(Solution.fibonacci(9))
# 34
