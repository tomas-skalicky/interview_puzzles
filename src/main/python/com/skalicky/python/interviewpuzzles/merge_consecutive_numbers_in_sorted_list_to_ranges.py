# Task:
#
# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.
#
# Example:
# Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
# Output: ['0->2', '5->5', '7->11', '15->15']
# Assume that all numbers will be greater than or equal to 0, and each element can repeat.
#
# Here is a starting point:
#
# def findRanges(nums):
#   # Fill this in.
#
# print findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15])
# # ['0->2', '5->5', '7->11', '15->15']
from typing import List


def find_ranges(nums: List[int]):
    number_count: int = len(nums)
    if number_count == 0:
        return []
    else:
        result: List[str] = []
        range_start: int = nums[0]
        previous_number: int = range_start
        for i in range(1, number_count):
            current_number: int = nums[i]
            if current_number > previous_number + 1:
                result.append('{}->{}'.format(range_start, previous_number))
                range_start = current_number
            previous_number = current_number
        result.append('{}->{}'.format(range_start, previous_number))
        return result


print(find_ranges([]))
# []
print(find_ranges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
