# Task:
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
# the non-zero elements.
#
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
# Here is a starting point:
#
# class Solution:
#   def moveZeros(self, nums):
#     # Fill this in.
#
# nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
# Solution().moveZeros(nums)
# print(nums)
# # [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
from typing import List


class Solution:
    @staticmethod
    def move_zeros_at_the_end_and_keep_order(numbers: List[int]) -> None:
        number_count: int = len(numbers)
        if number_count == 0:
            return
        else:
            current_index_of_nonzero_to_swap: int = 0
            current_index_of_zero_to_swap: int = 0
            while current_index_of_nonzero_to_swap < number_count and current_index_of_zero_to_swap < number_count:
                while current_index_of_nonzero_to_swap < number_count and numbers[
                    current_index_of_nonzero_to_swap] == 0:
                    current_index_of_nonzero_to_swap = current_index_of_nonzero_to_swap + 1
                while current_index_of_zero_to_swap < number_count and numbers[current_index_of_zero_to_swap] != 0:
                    current_index_of_zero_to_swap = current_index_of_zero_to_swap + 1
                if current_index_of_nonzero_to_swap < number_count and current_index_of_zero_to_swap < number_count:
                    temporary: int = numbers[current_index_of_zero_to_swap]
                    numbers[current_index_of_zero_to_swap] = numbers[current_index_of_nonzero_to_swap]
                    numbers[current_index_of_nonzero_to_swap] = temporary
                    current_index_of_zero_to_swap = current_index_of_zero_to_swap + 1
                    current_index_of_nonzero_to_swap = current_index_of_nonzero_to_swap + 1
