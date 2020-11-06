# Task:
#
# Given a 32-bit integer, swap the 1st and 2nd bit, 3rd and 4th bit, up til the 31st and 32nd bit.
#
# Here's some starting code and an example:
#
# def swap_bits(num):
#   # Fill this in.
#
# print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# # 0b01010101010101010101010101010101
from typing import List


def swap_bits_in_integer(input_integer: int) -> int:
    digits_as_strings: List[str] = list(bin(input_integer).split('b')[1])
    number_length: int = len(digits_as_strings)
    for i in range(0, number_length, +2):
        if i + 1 < number_length:
            temporary_storage: str = digits_as_strings[i + 1]
            digits_as_strings[i + 1] = digits_as_strings[i]
            digits_as_strings[i] = temporary_storage
    return int('0b' + ''.join(digits_as_strings), base=2)
