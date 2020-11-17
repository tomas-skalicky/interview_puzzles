# Task:
#
# Given two binary numbers represented as strings, return the sum of the two binary numbers as a new binary represented
# as a string. Do this without converting the whole binary string into an integer.
#
# Here's an example and some starter code.
#
# def sum_binary(bin1, bin2):
#   # Fill this in.
#
# print(sum_binary("11101", "1011"))
# # 101000
from typing import Tuple


def sum_binary_digits(binary_digit1: str, binary_digit2: str, overflow: bool) -> Tuple[str, bool]:
    if binary_digit1 == '1':
        if binary_digit2 == '1':
            if overflow:
                return '1', True
            else:
                return '0', True
        else:
            if overflow:
                return '0', True
            else:
                return '1', False
    else:
        if binary_digit2 == '1':
            if overflow:
                return '0', True
            else:
                return '1', False
        else:
            if overflow:
                return '1', False
            else:
                return '0', False


def sum_2_binary_numbers_without_converting_to_integer(binary_number1: str, binary_number2: str) -> str:
    overflow: bool = False
    index_in_number1: int = len(binary_number1) - 1
    index_in_number2: int = len(binary_number2) - 1
    result: str = ''
    while index_in_number1 >= 0 or index_in_number2 >= 0 or overflow:
        binary_digit1: str = binary_number1[index_in_number1] if index_in_number1 >= 0 else 0
        binary_digit2: str = binary_number2[index_in_number2] if index_in_number2 >= 0 else 0
        result_digit, overflow = sum_binary_digits(binary_digit1, binary_digit2, overflow)
        result = result_digit + result
        index_in_number1 -= 1
        index_in_number2 -= 1
    return result
