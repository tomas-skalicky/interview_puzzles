# Task:
#
# You are given an array of integers. Return the smallest positive integer that is not present in the array. The array
# may contain duplicate entries.
#
# For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist
# in the array.
#
# Your solution should run in linear time and use constant space.
#
# Here's your starting point:
#
# def first_missing_positive(nums):
#   # Fill this in.
#
# print first_missing_positive([3, 4, -1, 1])
# # 2

# Brainstorming:
#
# Solution with sorting using comparison:
# (1) sort the list with the comparison technique first
# (2) then find the first positive integer which is not in the sorted list
# Complexities depends on the algorithm. Let us pick a merge sort:
# Time complexity in the worst case: O(n log n) where n is the size of the input list
# Space complexity in the worst case: O(n) where n is the size of the input list
#
# Solution with radix sort:
# (1) create an auxiliary array of size of the input list plus 1
# (2) iterate through the list and put the current element in the auxiliary array if the current element is
#     a positive integer and is less or equal to the size of the input list.
#     Example: element 1 goes to the index 0,
#              element 2 goes to the index 1,
#              element -1 is skipped,
#              element n+1 is skipped because if there is an element n+1, there must be a positive integer < n
#              not being in the input list,
# (3) iterate through the auxiliary array and print out the index+1 of the first cell in the auxiliary array which
#     is not populated
# Complexities:
# Time complexity in the worst case: O(n) in case all elements are 1..n
# Space complexity in the worst case: O(n)
from typing import List


def first_missing_positive(nums: List[int]) -> int:
    number_count: int = len(nums)
    if number_count == 0:
        return 1
    else:
        radix_array: List[bool] = [False] * (number_count + 1)
        for i in range(0, number_count):
            current_number: int = nums[i]
            if current_number < 1:
                continue
            elif current_number > number_count:
                continue
            else:
                radix_array[current_number - 1] = True
        for i in range(0, number_count + 1):
            number_present: bool = radix_array[i]
            if not number_present:
                return i + 1


print(first_missing_positive([3, 4, -1, 1]))
# 2
print(first_missing_positive([3, 4, 2, -1, 1]))
# 5
print(first_missing_positive([3, 4, 2, 5, 1]))
# 6
print(first_missing_positive([1]))
# 2
print(first_missing_positive([3]))
# 1
print(first_missing_positive([-3]))
# 1
print(first_missing_positive([]))
# 1
