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


def merge_consecutive_numbers_in_sorted_list_to_ranges(input_numbers: List[int]) -> List[str]:
    number_count: int = len(input_numbers)
    if number_count == 0:
        return []
    else:
        result: List[str] = []
        range_start: int = input_numbers[0]
        previous_number: int = range_start
        for i in range(1, number_count):
            current_number: int = input_numbers[i]
            if current_number > previous_number + 1:
                result.append('{}->{}'.format(range_start, previous_number))
                range_start = current_number
            previous_number = current_number
        result.append('{}->{}'.format(range_start, previous_number))
        return result
