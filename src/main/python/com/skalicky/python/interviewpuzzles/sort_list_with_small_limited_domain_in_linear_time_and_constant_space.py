# Task:
#
# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
#
# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]
#
# Challenge: Try sorting the list using constant space.
#
# def sortNums(nums):
#   # Fill this in.
#
# print sortNums([3, 3, 2, 1, 3, 2, 1])
# # [1, 1, 2, 2, 3, 3, 3]
from typing import List


def sort_list_with_small_limited_domain_in_linear_time_and_constant_space(input_numbers: List[int]) -> List[int]:
    frequency: List[int] = [0, 0, 0]
    for current_number in input_numbers:
        frequency[current_number - 1] += 1
    result: List[int] = []
    for current_number in range(0, 3):
        for i in range(0, frequency[current_number]):
            result.append(current_number + 1)
    return result
