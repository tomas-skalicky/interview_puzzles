# Task:
#
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
# which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
#
# Here is the method signature:
#
# class Solution:
#   def minSubArrayLen(self, nums, s):
#     # Fill this in
#
# print Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7)
# # 2
import sys
from typing import List


class Solution:
    @staticmethod
    def min_sub_array_len(nums: List[int], s: int):
        found = False
        min_length = sys.maxsize
        current_sum = 0
        first_index = 0
        for current_index in range(0, len(nums)):
            current_number = nums[current_index]
            if current_number >= s:
                return 1
            else:
                current_sum += current_number
                while current_sum >= s:
                    found = True
                    min_length = min(min_length, current_index + 1 - first_index)
                    current_sum -= nums[first_index]
                    first_index += 1
        if found:
            return min_length
        else:
            return 0


print(Solution.min_sub_array_len([2, 3, 1, 2, 4, 3], 7))
# 2
print(Solution.min_sub_array_len([2, 3, 1, 2, 4, 3], 20))
# 0
print(Solution.min_sub_array_len([2, 3, 1, 2, 4, 3], 2))
# 1
print(Solution.min_sub_array_len([2, 5, -1, 2, 4, 3], 6))
# 2
