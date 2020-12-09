# Task:
#
# Given a list, find the k-th largest element in the list.
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5
# Here is a starting point:
#
# def find_kth_largest_number_in_list(nums, k):
#     # Fill this in.
#
# print find_kth_largest_number_in_list([3, 5, 2, 4, 6, 8], 3)
# # 5
from typing import List, Optional


def swap_items_in_list(i: int, j: int, numbers: List[int]) -> None:
    temp: int = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp


def bubble_sort_iteration(start_index: int, numbers: List[int]) -> None:
    j: int = start_index
    while j < len(numbers):
        if numbers[j - 1] > numbers[j]:
            swap_items_in_list(j - 1, j, numbers)
        j += 1


def find_kth_largest_number_in_list(numbers: List[int], k: int) -> Optional[int]:
    number_count: int = len(numbers)
    if number_count < k:
        return None
    else:
        first_unsorted_k_numbers: List[int] = numbers[:k]
        # Time complexity of this for-loop and sort O(k log k)
        k_largest_numbers_sorted_asc: List[int] = sorted(first_unsorted_k_numbers)
        # The time complexity of this for-loop is O(n * k)
        for i in range(k, number_count):
            if numbers[i] > k_largest_numbers_sorted_asc[0]:
                k_largest_numbers_sorted_asc[0] = numbers[i]
                bubble_sort_iteration(1, k_largest_numbers_sorted_asc)
        return k_largest_numbers_sorted_asc[0]
