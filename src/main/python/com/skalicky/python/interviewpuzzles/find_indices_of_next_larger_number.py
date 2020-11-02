# Task:
#
# Given a list of numbers, for each element find the next element that is larger than the current element. Return
# the answer as a list of indices. If there are no elements larger than the current element, then use -1 instead.
#
# Here's an example and some starter code:
#
# def larger_number(nums):
#   # Fill this in.
#
# # print [2, 2, 3, 4, -1, -1]
# print(larger_number([3, 2, 5, 6, 9, 8]))
from bisect import insort_left
from typing import List, Dict


# Time complexity ... O(n log n) where n is a size of the input list
def larger_number(nums: List[int]) -> List[int]:
    result_indices: List[int] = [-1 for i in range(0, len(nums))]
    index_lists_by_searched_closest_larger_numbers: Dict[int, List[int]] = {}
    searched_closest_larger_numbers: List[int] = []
    for i in range(0, len(nums)):
        current_number: int = nums[i]
        # Each element in the list will be processed by the inner for loop at most once.
        while len(searched_closest_larger_numbers) > 0:
            searched_number: int = searched_closest_larger_numbers.pop(0)
            if searched_number <= current_number:
                for non_processed_index in index_lists_by_searched_closest_larger_numbers.pop(searched_number):
                    result_indices[non_processed_index] = i
            else:
                searched_closest_larger_numbers.insert(0, searched_number)
                break

        searched_closest_larger_number: int = current_number + 1
        if searched_closest_larger_numbers.__contains__(searched_closest_larger_number):
            index_lists_by_searched_closest_larger_numbers[searched_closest_larger_number].append(i)
        else:
            # Time complexity ... O(log n)
            insort_left(searched_closest_larger_numbers, searched_closest_larger_number)
            index_lists_by_searched_closest_larger_numbers[searched_closest_larger_number] = [i]

    return result_indices
