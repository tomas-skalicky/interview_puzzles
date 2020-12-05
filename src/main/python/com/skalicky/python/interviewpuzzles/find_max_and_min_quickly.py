# Task:
#
# Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of the list using less than
# 2 * (n - 1) comparisons.
#
# Here's a start:
#
# def find_max_and_min_quickly(numbers):
#     # Fill this in.
#
# print find_max_and_min_quickly([3, 5, 1, 2, 4, 8])
# # (1, 8, 9)
# # where 9 is the maximum allowed number of comparisons
from typing import List, Tuple


def find_max_and_min_quickly(numbers: List[int]) -> Tuple[int, int, int]:
    comparison_count_in_worst_case: int = 0
    current_min: int = numbers[0]
    current_max: int = numbers[0]
    current_number: int = numbers[1]
    if current_number < current_min:
        current_min = current_number
    else:
        current_max = current_number
    comparison_count_in_worst_case += 1

    number_count: int = len(numbers)
    for i in range(2, number_count):
        current_number = numbers[i]
        if current_number < current_min:
            current_min = current_number
        elif current_number > current_max:
            current_max = current_number
        comparison_count_in_worst_case += 2
    return current_min, current_max, comparison_count_in_worst_case
