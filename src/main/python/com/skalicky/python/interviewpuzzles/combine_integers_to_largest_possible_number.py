# Task:
#
# Given a number of integers, combine them so it would create the largest number.
#
# Example:
# Input:  [17, 7, 2, 45, 72]
# Output:  77245217
# def combine_integers_to_largest_possible_number(nums):
#     # Fill this in.
#
# print combine_integers_to_largest_possible_number([17, 7, 2, 45, 72])
# # 77245217
from functools import cmp_to_key
from typing import List


def compare(number1_string: str, number2_string: str) -> int:
    num1_first_digit: str = number1_string[0]
    num1_length: int = len(number1_string)
    num2_first_digit: str = number2_string[0]
    num2_length: int = len(number2_string)
    adapted_num1_str: str = number1_string if num1_length >= num2_length else number1_string + (
            num1_first_digit * (num2_length - num1_length))
    adapted_num2_str: str = number2_string if num2_length >= num1_length else number2_string + (
            num2_first_digit * (num1_length - num2_length))
    if adapted_num1_str < adapted_num2_str:
        return -1
    elif adapted_num1_str > adapted_num2_str:
        return 1
    else:
        return 0


def combine_integers_to_largest_possible_number(numbers: List[int]) -> str:
    num_strings: List[str] = [str(n) for n in numbers]
    sorted_num_strings: List[str] = sorted(num_strings, key=cmp_to_key(compare), reverse=True)
    return ''.join(sorted_num_strings)
