# Task:
#
# Write a function that reverses the digits a 32-bit signed integer, x. Assume that the environment can only store
# integers within the 32-bit signed integer range, [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer
# overflows.
#
# Example:
# Input: 123
# Output: 321
# class Solution:
#   def reverse(self, x):
#     # Fill this in.
#
# print(Solution().reverse(123))
# # 321
# print(Solution().reverse(2**31))
# # 0
from typing import List


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        input_digits: List[int] = list(str(x))
        result_digits: List[int] = []
        for i in reversed(range(0, len(input_digits))):
            result_digits.append(input_digits[i])
        result_string: str = ''.join([str(digit) for digit in result_digits])
        max_number_string: str = '2147483648'
        if len(result_string) >= len(max_number_string) and result_string > max_number_string:
            return 0
        else:
            return int(result_string)


print(Solution.reverse(123))
# 321
print(Solution.reverse(2 ** 31))
# 0
print(Solution.reverse(2147483642))
# 0
