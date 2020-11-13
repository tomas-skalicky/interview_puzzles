# Task:
#
# Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in
# both arrays.
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique.
# The result can be in any order.
#
# Here's a starting point:
#
# class Solution:
#   def intersection(self, nums1, nums2):
#     # Fill this in.
#
# print Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])
# # [9, 4]
from typing import Set, List


class Solution:
    @staticmethod
    def find_intersection_set_of_two_arrays(array1: List[int], array2: List[int]) -> Set[int]:
        set1: Set[int] = set(array1)
        result_set: Set[int] = set()
        for number2 in array2:
            if number2 in set1:
                result_set.add(number2)
        return result_set
