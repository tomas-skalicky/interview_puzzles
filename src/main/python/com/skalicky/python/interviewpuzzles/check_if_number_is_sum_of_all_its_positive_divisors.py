# Task:
#
# A Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
#
# For instance,
# 28 = 1 + 2 + 4 + 7 + 14
#
# Write a function to determine if a number is a perfect number.
#
# class Solution:
#     @staticmethod
#     def check_if_number_is_sum_of_all_its_positive_divisors(number):
#         # Fill this in.
#
# print(Solution.check_if_number_is_sum_of_all_its_positive_divisors(28))
# # True
# # 28 = 1 + 2 + 4 + 7 + 14
from math import floor, sqrt


class Solution:
    @staticmethod
    def check_if_number_is_sum_of_all_its_positive_divisors(number: int) -> bool:
        if number < 2:
            return False
        else:
            current_sum: int = 1
            max_smaller_divisor: int = floor(sqrt(number))
            divisor_candidate: int = 2
            while divisor_candidate <= max_smaller_divisor:
                if number % divisor_candidate == 0:
                    larger_divisor: int = floor(number / divisor_candidate)
                    current_sum += divisor_candidate + larger_divisor
                    if current_sum > number:
                        return False
                divisor_candidate += 1
            return current_sum == number
