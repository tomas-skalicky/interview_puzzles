# Task:
#
# Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of the list using less than
# 2 * (n - 1) comparisons.
#
# Here's a start:
#
# def find_min_max(nums):
#   # Fill this in.
#
# print find_min_max([3, 5, 1, 2, 4, 8])
# # (1, 8)
from typing import List, Tuple


def find_min_max(nums: List[int]) -> Tuple[int, int]:
    comparison_count_in_worst_case: int = 0
    current_min: int = nums[0]
    current_max: int = nums[0]
    current_number: int = nums[1]
    if current_number < current_min:
        current_min = current_number
    else:
        current_max = current_number
    comparison_count_in_worst_case += 1

    number_count: int = len(nums)
    for i in range(2, number_count):
        current_number = nums[i]
        if current_number < current_min:
            current_min = current_number
        elif current_number > current_max:
            current_max = current_number
        comparison_count_in_worst_case += 2
    print('The number of comparisons must be less than {}. comparison_count_in_worst_case={}'.format(
        2 * (number_count - 1),
        comparison_count_in_worst_case))
    return current_min, current_max


print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)
