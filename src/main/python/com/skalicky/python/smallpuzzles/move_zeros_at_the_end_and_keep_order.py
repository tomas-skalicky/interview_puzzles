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
    def move_zeros(self, nums: List[int]):
        num_count: int = len(nums)
        if num_count == 0:
            return
        else:
            current_index_of_nonzero_to_swap: int = 0
            current_index_of_zero_to_swap: int = 0
            while current_index_of_nonzero_to_swap < num_count and current_index_of_zero_to_swap < num_count:
                while current_index_of_nonzero_to_swap < num_count and nums[current_index_of_nonzero_to_swap] == 0:
                    current_index_of_nonzero_to_swap = current_index_of_nonzero_to_swap + 1
                while current_index_of_zero_to_swap < num_count and nums[current_index_of_zero_to_swap] != 0:
                    current_index_of_zero_to_swap = current_index_of_zero_to_swap + 1
                if current_index_of_nonzero_to_swap < num_count and current_index_of_zero_to_swap < num_count:
                    temporary: int = nums[current_index_of_zero_to_swap]
                    nums[current_index_of_zero_to_swap] = nums[current_index_of_nonzero_to_swap]
                    nums[current_index_of_nonzero_to_swap] = temporary
                    current_index_of_zero_to_swap = current_index_of_zero_to_swap + 1
                    current_index_of_nonzero_to_swap = current_index_of_nonzero_to_swap + 1


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().move_zeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
nums2 = []
Solution().move_zeros(nums2)
print(nums2)
# []
nums3 = [2, 1]
Solution().move_zeros(nums3)
print(nums3)
# [2, 1]
nums4 = [0, 0]
Solution().move_zeros(nums4)
print(nums4)
# [0, 0]
