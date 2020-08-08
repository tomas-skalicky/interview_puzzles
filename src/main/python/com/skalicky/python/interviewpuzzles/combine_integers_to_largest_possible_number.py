# Task:
#
# Given a number of integers, combine them so it would create the largest number.
#
# Example:
# Input:  [17, 7, 2, 45, 72]
# Output:  77245217
# def largestNum(nums):
#   # Fill this in.
#
# print largestNum([17, 7, 2, 45, 72])
# # 77245217
from typing import List
from functools import cmp_to_key


def compare(num1_str: str, num2_str: str) -> int:
    num1_first_digit: str = num1_str[0]
    num1_length: int = len(num1_str)
    num2_first_digit: str = num2_str[0]
    num2_length: int = len(num2_str)
    adapted_num1_str: str = num1_str if num1_length >= num2_length else num1_str + (
            num1_first_digit * (num2_length - num1_length))
    adapted_num2_str: str = num2_str if num2_length >= num1_length else num2_str + (
            num2_first_digit * (num1_length - num2_length))
    if adapted_num1_str < adapted_num2_str:
        return -1
    elif adapted_num1_str > adapted_num2_str:
        return 1
    else:
        return 0


def largest_num(nums: List[int]) -> str:
    num_strings: List[str] = [str(n) for n in nums]
    sorted_num_strings: List[str] = sorted(num_strings, key=cmp_to_key(compare), reverse=True)
    return ''.join(sorted_num_strings)


print(largest_num([17, 7, 2, 45, 72]))
# 77245217
print(largest_num([7, 78, 72]))
# 78772
