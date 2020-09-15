# Task:
#
# Given a list of numbers, find the smallest window to sort such that the whole list will be sorted. If the list is
# already sorted return (0, 0). You can assume there will be no duplicate numbers.
#
# Example:
#
# Input: [2, 4, 7, 5, 6, 8, 9]
# Output: (2, 4)
#
# Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that the whole list is sorted.
#
# def min_window_to_sort(nums):
#   # Fill this in.
#
# print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# # (2, 4)
from typing import List, Tuple


def min_window_to_sort(nums: List[int]) -> Tuple[int, int]:
    nums_size: int = len(nums)
    if nums_size < 2:
        return 0, 0
    else:
        min_index_of_larger_than_right: int = None
        max_larger_than_right: int = None
        index_of_current_window_end: int = None
        for i in range(0, nums_size - 1):
            current_number: int = nums[i]
            next_number: int = nums[i + 1]

            if next_number < current_number:
                max_larger_than_right = max(max_larger_than_right,
                                            current_number) if max_larger_than_right is not None else current_number
                if min_index_of_larger_than_right is None:
                    min_index_of_larger_than_right = i
            elif max_larger_than_right is not None and current_number < max_larger_than_right < next_number:
                index_of_current_window_end = i

        if min_index_of_larger_than_right is None and index_of_current_window_end is None:
            return 0, 0
        elif min_index_of_larger_than_right is not None and index_of_current_window_end is None:
            return min_index_of_larger_than_right, nums_size - 1
        else:
            return min_index_of_larger_than_right, index_of_current_window_end


print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
print(min_window_to_sort([2, 7, 3, 4, 5, 6, 8, 9, 10]))
# (1, 5)
print(min_window_to_sort([7, 3, 5, 8, 9]))
# (0, 2)
print(min_window_to_sort([2, 7, 3, 5]))
# (1, 3)
print(min_window_to_sort([7, 5, 6]))
# (0, 2)
print(min_window_to_sort([5, 6]))
# (0, 0)
print(min_window_to_sort([2, 5, 3, 4, 6, 8, 7, 9]))
# (1, 6)
print(min_window_to_sort([2]))
# (0, 0)
