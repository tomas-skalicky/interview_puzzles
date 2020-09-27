# Task:
#
# Kaprekar's Constant is the number 6174. This number is special because it has the property where for any 4-digit
# number that has 2 or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.
#
# This certain function is as follows:
# - Order the number in ascending form and descending form to create 2 numbers.
# - Pad the descending number with zeros until it is 4 digits in length.
# - Subtract the ascending number from the descending number.
# - Repeat.
#
# Given a number n, find the number of times the function needs to be applied to reach Kaprekar's constant. Here's some
# starter code:
#
# KAPREKAR_CONSTANT = 6174
#
# def num_kaprekar_iterations(n):
#   # Fill this in.
#
# print num_kaprekar_iterations(123)
# # 3
# # Explanation:
# #  3210 - 123 = 3087
# #  8730 - 0378 = 8352
# #  8532 - 2358 = 6174 (3 iterations)
from typing import List

KAPREKAR_CONSTANT = 6174


def num_kaprekar_iterations(n: int) -> int:
    current_number: int = n
    iteration_count: int = 0
    while current_number != KAPREKAR_CONSTANT:
        iteration_count += 1
        current_number_as_list: List[str] = list(str(current_number))
        while len(current_number_as_list) < 4:
            current_number_as_list.append('0')
        ascending_number: int = int(''.join(sorted(current_number_as_list)))
        descending_number: int = int(''.join(sorted(current_number_as_list, reverse=True)))
        current_number = descending_number - ascending_number
    return iteration_count


print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
