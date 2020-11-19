# Task:
#
# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.
#
# Here's some examples and some starter code.
#
# def reverse_integer(num):
#   # Fill this in.
#
# print(reverse_integer(135))
# # 531
#
# print(reverse_integer(-321))
# # -123
from math import floor


def reverse_integer_without_converting_it_to_string(input_number: int) -> int:
    rest: int = input_number
    negative: bool = rest < 0
    if negative:
        rest *= -1

    result: int = 0
    while rest > 0:
        new_rest: int = floor(rest / 10)
        result = result * 10 + rest % 10
        rest = new_rest
    return result * (-1 if negative else 1)
