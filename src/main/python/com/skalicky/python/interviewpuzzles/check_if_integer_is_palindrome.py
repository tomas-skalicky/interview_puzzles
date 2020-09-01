# Task:
#
# Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to
# check if it is a palindrome.
#
# import math
#
# def is_palindrome(n):
#   # Fill this in.
#
# print is_palindrome(1234321)
# # True
# print is_palindrome(1234322)
# # False


import math


def is_palindrome(n: int) -> bool:
    rest: int = n
    reversed_number: int = 0
    while rest > 0:
        current_last_digit: int = rest % 10
        reversed_number = reversed_number * 10 + current_last_digit
        rest = int(rest / 10)
    return n == reversed_number


print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
