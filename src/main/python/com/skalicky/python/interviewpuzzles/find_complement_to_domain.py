# Task:
#
# Given an array of integers of size n, where all elements are between 1 and n inclusive, find all of the elements of
# [1, n] that do not appear in the array. Some numbers may appear more than once.
#
# Example:
# Input: [4,5,2,6,8,2,1,5]
# Output: [3,7]
# class Solution(object):
#   def findDisappearedNumbers(self, nums):
#     # Fill this in.
#
# nums = [4, 6, 2, 6, 7, 2, 1]
# print(Solution().findDisappearedNumbers(nums))
# # [3, 5]
#
# For this problem, you can assume that you can mutate the input array.
from typing import List, Set


class Solution(object):
    @staticmethod
    def find_disappeared_numbers(nums: List[int]) -> List[int]:
        complement_to_domain: Set[int] = set(range(1, len(nums) + 1))
        for n in nums:
            if complement_to_domain.__contains__(n):
                complement_to_domain.remove(n)
        return list(complement_to_domain)


print(Solution.find_disappeared_numbers([4, 6, 2, 6, 7, 2, 1]))
# [3, 5]
