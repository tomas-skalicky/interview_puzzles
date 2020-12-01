# Task:
#
# Given a list of positive numbers, find the largest possible set such that no elements are adjacent numbers of each
# other.
#
# Here's some example and some starter code
#
# def maxNonAdjacentSum(nums):
#   # Fill this in.
#
# print(maxNonAdjacentSum([3, 4, 1, 1]))
# # [4, 1]
# # max sum is 4 (index 1) + 1 (index 3)
#
# print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
# # [2, 7]
# # max sum is 2 (index 0) + 7 (index 3)
from collections import deque
from typing import Deque, List, Tuple


def find_sublist_of_non_adjacent_numbers_with_largest_sum(numbers: List[int]) -> List[int]:
    """Time complexity ... O(2 ^ n) where *n* is the length of the input List. Reason: every (second) number can, but
    does not need to be a part of the result sub-list.
    """

    number_count: int = len(numbers)

    intermediate_sum_and_sublist_and_index_to_process: Deque[Tuple[int, List[int], int]] = deque()
    current_maximum_sum: int = 0
    sublist_with_current_maximum_sum: List[int] = []
    intermediate_sum_and_sublist_and_index_to_process.append(
        (current_maximum_sum, sublist_with_current_maximum_sum, 0))

    while len(intermediate_sum_and_sublist_and_index_to_process) > 0:
        intermediate_sum, sublist, index_to_process = intermediate_sum_and_sublist_and_index_to_process.popleft()
        if index_to_process >= number_count:
            if intermediate_sum > current_maximum_sum:
                current_maximum_sum = intermediate_sum
                sublist_with_current_maximum_sum = sublist
            pass
        else:
            current_number: int = numbers[index_to_process]

            new_sublist: List[int] = sublist.copy()
            new_sublist.append(current_number)
            intermediate_sum_and_sublist_and_index_to_process.append(
                (intermediate_sum + current_number, new_sublist, index_to_process + 2))

            intermediate_sum_and_sublist_and_index_to_process.append(
                (intermediate_sum, sublist, index_to_process + 1))

    return sublist_with_current_maximum_sum
