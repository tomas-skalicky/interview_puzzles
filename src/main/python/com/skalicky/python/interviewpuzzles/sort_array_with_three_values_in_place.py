# Task:
#
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
# adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library’s sort function for this problem.
#
# Can you do this in a single pass?
#
# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Here's a starting point:
#
# class Solution:
#   def sortColors(self, nums):
#     # Fill this in.
#
# nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
# print("Before Sort: ")
# print(nums)
# # [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
#
# Solution().sortColors(nums)
# print("After Sort: ")
# print(nums)
# # [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
from math import floor
from typing import List


class Solution:
    @staticmethod
    def sort_colors(numbers: List[int]):
        number_count: int = len(numbers)
        if number_count > 1:
            last_zero_index: int = -1
            last_one_index: int = -1
            first_two_index: int = number_count
            while last_one_index + 1 < first_two_index:
                current_number: int = numbers[last_one_index + 1]
                if current_number == 0:
                    last_zero_index += 1
                    last_one_index += 1
                    if last_zero_index != last_one_index:
                        numbers[last_zero_index] = 0
                        numbers[last_one_index] = 1
                elif current_number == 1:
                    last_one_index += 1
                else:
                    first_two_index -= 1
                    numbers[last_one_index + 1] = numbers[first_two_index]
                    numbers[first_two_index] = current_number
        return numbers


def sort_and_print(numbers: List[int]):
    print('Before Sort: {}'.format(numbers))
    Solution.sort_colors(numbers)
    print('After Sort:  {}'.format(numbers), end='\n\n')


sort_and_print([])
# []

sort_and_print([0])
# [0]

sort_and_print([0, 1])
# [0, 1]

sort_and_print([0, 2, 1])
# [0, 2, 1]

sort_and_print([1, 1, 1])
# [1, 1, 1]

sort_and_print([2, 1, 0])
# [0, 1, 2]

sort_and_print([0, 0, 1, 1, 2, 2])
# [0, 0, 1, 1, 2, 2]

sort_and_print([0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1])
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
