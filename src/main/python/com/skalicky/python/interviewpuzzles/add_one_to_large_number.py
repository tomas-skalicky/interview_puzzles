# Task:
#
# Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer.
# The most significant digit is at the front of the array and each element in the array contains only one digit.
# Furthermore, the integer does not have leading zeros, except in the case of the number '0'.
#
# Example:
# Input: [2,3,4]
# Output: [2,3,5]
# class Solution():
#   def plusOne(self, digits):
#     # Fill this in.
#
# num = [2, 9, 9]
# print(Solution().plusOne(num))
# # [3, 0, 0]
from typing import List


class Solution:
    @staticmethod
    def add_one_to_large_number(large_number_digits: List[int]) -> List[int]:
        new_large_number_digits: List[int] = []
        overflow: int = 0
        first: bool = True
        for n in reversed(large_number_digits):
            new_numbers: int = n
            if first:
                first = False
                new_numbers += 1
            else:
                new_numbers += overflow
            overflow = int(new_numbers / 10)
            new_large_number_digits.append(new_numbers % 10)
        if overflow > 0:
            new_large_number_digits.append(overflow)
        new_large_number_digits.reverse()
        return new_large_number_digits
