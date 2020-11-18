# Task:
#
# Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset
# in the list.
#
# Example:
# Input: [1, 2, 3, 8, 9, 10]
# Output: 7
# Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.
#
# def findSmallest(nums):
#   # Fill this in.
#
# print findSmallest([1, 2, 3, 8, 9, 10])
# # 7
from typing import List, Set


def find_smallest(nums: List[int]) -> int:
    current_smallest: int = 1
    interim_sums: Set[int] = set()
    for n in nums:
        if current_smallest < n:
            return current_smallest
        else:
            new_sums: Set[int] = set()
            if n == current_smallest:
                new_sums.add(n)
            for interim_sum in interim_sums:
                new_sum: int = interim_sum + n
                if new_sum >= current_smallest:
                    new_sums.add(new_sum)
                    new_sums.add(interim_sum)
            interim_sums = new_sums
            while current_smallest in interim_sums:
                current_smallest += 1
    return current_smallest


print(find_smallest([]))
# 1
print(find_smallest([1, 2, 3, 7]))
# 14
print(find_smallest([1, 2, 3, 8, 9, 10]))
# 7
