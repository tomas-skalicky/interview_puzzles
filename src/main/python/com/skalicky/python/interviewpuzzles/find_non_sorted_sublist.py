# Task:
#
# Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be
# sorted.
#
# Example:
# Input: [1, 7, 9, 5, 7, 8, 10]
# Output: (1, 5)
# Explanation:
# The numbers between index 1 and 5 are out of order and need to be sorted.
#
# Here's your starting point:
#
# def findRange(nums):
#   # Fill this in.
#
# print findRange([1, 7, 9, 5, 7, 8, 10])
# # (1, 5)
from typing import List, Tuple


# A trivial algorithm would perform a sort of input list and would compare the sorted list with input list. This
# algorithm would have a time complexity of O(n * log n).
#
# The implemented algorithm has a time complexity of O(n).
def find_range(nums: List[int]) -> Tuple[int, int]:
    number_count: int = len(nums)
    if number_count == 0:
        return None
    else:
        sorted_till_index_from_left: int = 0
        sorted_till_value_from_left: int = nums[sorted_till_index_from_left]
        for i in range(1, number_count):
            current_number: int = nums[i]
            while sorted_till_value_from_left is not None and current_number < sorted_till_value_from_left:
                sorted_till_index_from_left -= 1
                sorted_till_value_from_left = nums[
                    sorted_till_index_from_left] if sorted_till_index_from_left >= 0 else None
            if sorted_till_index_from_left == i - 1 and current_number > sorted_till_value_from_left:
                sorted_till_index_from_left = i
                sorted_till_value_from_left = current_number

        if sorted_till_index_from_left == number_count - 1:
            return None
        else:
            sorted_till_index_from_right: int = number_count - 1
            sorted_till_value_from_right: int = nums[sorted_till_index_from_right]
            for i in reversed(range(sorted_till_index_from_left + 2, number_count - 1)):
                current_number: int = nums[i]
                while sorted_till_value_from_right is not None and current_number > sorted_till_value_from_right:
                    sorted_till_index_from_right += 1
                    sorted_till_value_from_right = nums[
                        sorted_till_index_from_right] if sorted_till_index_from_right < number_count else None
                if sorted_till_index_from_right == i + 1 and current_number < sorted_till_value_from_right:
                    sorted_till_index_from_right = i
                    sorted_till_value_from_right = current_number
            return sorted_till_index_from_left + 1, sorted_till_index_from_right - 1


print(find_range([]))
# None
print(find_range([1]))
# None
print(find_range([1, 7, 10]))
# None
print(find_range([10, 7, 1]))
# (0, 2)
print(find_range([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
