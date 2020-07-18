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
from collections.abc import Set, MutableSet


class Solution:
    @staticmethod
    def intersection(nums1, nums2):
        nums1_set: Set[int] = set(nums1)
        result_set: MutableSet[int] = set()
        for n in nums2:
            if nums1_set.__contains__(n):
                result_set.add(n)
        return list(result_set)


print(Solution.intersection([1, 2, 2, 1], [2, 2]))
# [2]
print(Solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]
