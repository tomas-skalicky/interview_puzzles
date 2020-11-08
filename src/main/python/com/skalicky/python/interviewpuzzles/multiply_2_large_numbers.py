# Task:
#
# Given two strings which represent non-negative integers, multiply the two numbers and return the product as a string
# as well. You should assume that the numbers may be sufficiently large such that the built-in integer type will not
# be able to store the input (Python does have BigNum, but assume it does not exist).
#
# Here's an example and some starter code.
#
# def multiply(str1, str2):
#   # Fill this in.
from collections import deque
from typing import List, Deque


def multiply_2_large_numbers(number1_string: str, number2_string: str) -> str:
    if number1_string == '0' or number2_string == '0':
        return '0'
    else:
        number1_digits_reversed: List[str] = list(number1_string)
        number1_digits_reversed.reverse()
        number2_digits_reversed: List[str] = list(number2_string)
        number2_digits_reversed.reverse()
        reversed_intermediate_multiplications: Deque[str] = deque()
        trailing_zeros: str = ''
        for number1_digit_string in number1_digits_reversed:
            overflow: int = 0
            reversed_intermediate_multiplication: str = trailing_zeros
            for number2_digit_string in number2_digits_reversed:
                intermediate_result: int = int(number1_digit_string) * int(number2_digit_string) + overflow
                digit_to_add: int = intermediate_result % 10
                reversed_intermediate_multiplication += str(digit_to_add)
                overflow = int((intermediate_result - digit_to_add) / 10)
            reversed_intermediate_multiplications.append(reversed_intermediate_multiplication)
            trailing_zeros += '0'

        result: str = ''
        intermediate_multiplication_count: int = len(reversed_intermediate_multiplications)
        max_length: int = len(reversed_intermediate_multiplications[intermediate_multiplication_count - 1])
        overflow: int = 0
        for i in range(0, max_length):

            remove_first: bool = False
            first_processed: bool = False
            intermediate_sum: int = overflow
            for reversed_intermediate_multiplication in reversed_intermediate_multiplications:
                if i < len(reversed_intermediate_multiplication):
                    intermediate_sum += int(reversed_intermediate_multiplication[i])
                if first_processed:
                    first_processed = True
                    if i >= len(reversed_intermediate_multiplication):
                        remove_first = True

            digit_to_add: int = intermediate_sum % 10
            result = str(digit_to_add) + result
            overflow = int((intermediate_sum - digit_to_add) / 10)

            if remove_first:
                reversed_intermediate_multiplications.pop()
        return result
