# Task:
#
# A UTF-8 character encoding is a variable width character encoding that can vary from 1 to 4 bytes depending on
# the character. The structure of the encoding is as follows:
# 1 byte:  0xxxxxxx
# 2 bytes: 110xxxxx 10xxxxxx
# 3 bytes: 1110xxxx 10xxxxxx 10xxxxxx
# 4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# For more information, you can read up on the Wikipedia Page.
#
# Given a list of integers where each integer represents 1 byte, return whether or not the list of integers is a valid
# UTF-8 encoding.
#
# BYTE_MASKS = [
#     None,
#     0b10000000,
#     0b11100000,
#     0b11110000,
#     0b11111000,
# ]
# BYTE_EQUAL = [
#     None,
#     0b00000000,
#     0b11000000,
#     0b11100000,
#     0b11110000,
# ]
#
# def utf8_validator(bytes):
#   # Fill this in.
#
# print utf8_validator([0b00000000])
# # True
# print utf8_validator([0b00000000, 10000000])
# # False
# print utf8_validator([0b11000000, 10000000])
# # True
from typing import List

BYTE_MASKS = [
    None,
    0b10000000,
    0b11100000,
    0b11110000,
    0b11111000,
]
BYTE_EQUAL = [
    None,
    0b00000000,
    0b11000000,
    0b11100000,
    0b11110000,
]


def utf8_validator(input_bytes: List[int]) -> bool:
    input_length: int = len(input_bytes)
    i: int = 0
    while i < input_length:
        current_byte: int = input_bytes[i]
        if current_byte not in BYTE_EQUAL:
            return False
        else:
            encoding_length: int = BYTE_EQUAL.index(input_bytes[i])
            for index_of_further_bytes in range(0, encoding_length - 1):
                i += 1
                if i == input_length:
                    return False
                else:
                    current_non_first_byte: int = input_bytes[i]
                    if current_non_first_byte < 10000000 or current_non_first_byte > 10111111:
                        return False
            i += 1
    return True


print(utf8_validator([0b00000000]))
# True
print(utf8_validator([0b00000000, 10000000]))
# False
print(utf8_validator([0b11000000, 10000000]))
# True
print(utf8_validator([0b11000000, 10000000, 0b11100000, 10000000, 10000000]))
# True
print(utf8_validator([0b11000000, 10000000, 0b11100000, 10000000]))
# False
print(utf8_validator([0b11000000, 10100000]))
# True
print(utf8_validator([0b11000000, 11000000]))
# False
print(utf8_validator([0b11000000, 1111111]))
# False
