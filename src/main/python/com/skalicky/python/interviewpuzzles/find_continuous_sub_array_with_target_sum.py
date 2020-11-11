# Task:
#
# You are given an array of integers, and an integer K. Return the subarray which sums to K. You can assume that
# a solution will always exist.
#
# def find_continuous_k(list, k):
#   # Fill this in.
#
# print find_continuous_k([1, 3, 2, 5, 7, 2], 14)
# # [2, 5, 7]
#
# Can you do this in linear time?
from typing import List, Optional


def find_continuous_sub_array_with_target_sum(input_list: List[int], k: int) -> Optional[List[int]]:
    current_start_index_included: int = 0
    current_end_index_included: int = 0
    current_sum: int = input_list[current_start_index_included]
    input_size: int = len(input_list)
    while current_sum != k and current_end_index_included + 1 < input_size:
        current_end_index_included += 1
        current_sum += input_list[current_end_index_included]
        while current_sum > k:
            current_sum -= input_list[current_start_index_included]
            current_start_index_included += 1
    if current_sum == k:
        return input_list[current_start_index_included:current_end_index_included + 1]
    else:
        return None
