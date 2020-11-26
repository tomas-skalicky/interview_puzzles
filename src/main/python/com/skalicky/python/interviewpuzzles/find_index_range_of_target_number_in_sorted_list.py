# Task:
#
# Given a sorted list with duplicates, and a target number n, find the index range in which the number exists
# (represented as a tuple (low, high), both inclusive. If the number does not exist in the list, return (-1, -1)).
#
# Here's some examples and some starter code.
#
# def find_index_range_of_target_number_in_sorted_list(numbers, target_number):
#     # Fill this in.
#
# print(find_index_range_of_target_number_in_sorted_list([1, 1, 3, 5, 7], 1))
# # (0, 1)
#
# print(find_index_range_of_target_number_in_sorted_list([1, 2, 3, 4], 5))
# # (-1, -1)
from bisect import bisect_left
from typing import List, Tuple


def find_index_range_of_target_number_in_sorted_list(numbers: List[int], target_number: int) -> Tuple[int, int]:
    """Time complexity ... O(log n) if the target number is in the input only once. O(n) if the input contains only
    target number (possibly multiple times) and nothing else.
    """

    number_count: int = len(numbers)
    if number_count == 0:
        return -1, -1

    else:
        min_index: int = bisect_left(numbers, target_number)
        if min_index < 0 or min_index >= number_count:
            return -1, -1

        else:
            max_index: int = min_index
            while max_index + 1 < number_count and numbers[max_index + 1] == target_number:
                max_index += 1
            return min_index, max_index
