# Task:
#
# MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB,
# ... etc. In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA" and so forth.
# Given a positive integer, find its corresponding column name.
# Examples:
# Input: 26
# Output: Z
#
# Input: 51
# Output: AY
#
# Input: 52
# Output: AZ
#
# Input: 676
# Output: YZ
#
# Input: 702
# Output: ZZ
#
# Input: 704
# Output: AAB
# Here is a starting point:
#
# class Solution:
#   def convertToTitle(self, n):
#     # Fill this in.
#
# input1 = 1
# input2 = 456976
# input3 = 28
# print(Solution().convertToTitle(input1))
# # A
# print(Solution().convertToTitle(input2))
# # YYYZ
# print(Solution().convertToTitle(input3))
# # AB


ALPHABET_SIZE: int = 26


class Solution:
    @staticmethod
    def convert_to_title(n: int) -> str:
        result_name: str = ''
        current_number: int = n
        while current_number > 0:
            current_letter_in_int: int = (current_number - 1) % ALPHABET_SIZE + 1
            current_letter: str = chr(current_letter_in_int + 64)
            result_name = current_letter + result_name
            current_number -= current_letter_in_int
            current_number = int(current_number / ALPHABET_SIZE)
        return result_name


print(Solution.convert_to_title(1))
# A
print(Solution.convert_to_title(26))
# Z
print(Solution.convert_to_title(456976))
# YYYZ
print(Solution.convert_to_title(28))
# AB
print(Solution.convert_to_title(51))
# AY
print(Solution.convert_to_title(52))
# AZ
print(Solution.convert_to_title(676))
# YZ
print(Solution.convert_to_title(702))
# ZZ
print(Solution.convert_to_title(704))
# AAB
