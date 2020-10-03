# Task:
#
# Given a Roman numeral, find the corresponding decimal value. Inputs will be between 1 and 3999.
#
# Example:
# Input: IX
# Output: 9
#
# Input: VII
# Output: 7
#
# Input: MCMIV
# Output: 1904
# Roman numerals are based on the following symbols:
# I     1
# IV    4
# V     5
# IX    9
# X     10
# XL    40
# L     50
# XC    90
# C     100
# CD    400
# D     500
# CM    900
# M     1000
# Numbers are strings of these symbols in descending order. In some cases, subtractive notation is used to avoid
# repeated characters. The rules are as follows:
# 1.) I placed before V or X is one less, so 4 = IV (one less than 5), and 9 is IX (one less than 10)
# 2.) X placed before L or C indicates ten less, so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).
# 3.) C placed before D or M indicates 100 less, so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000).
#
# class Solution:
#   def romanToInt(self, s):
#     # Fill this in.
#
# n = 'MCMX'
# print(Solution.romanToInt(n))
# # 1910
from typing import Optional


class Solution:
    @staticmethod
    def roman_to_int(s) -> int:
        result: int = 0
        processed_previous_letter: Optional[str] = None
        for letter in list(s):
            if letter == 'I':
                result += 1
            elif letter == 'V' or letter == 'X':
                if processed_previous_letter == 'I':
                    result += 3 if letter == 'V' else 8
                else:
                    result += 5 if letter == 'V' else 10
            elif letter == 'L' or letter == 'C':
                if processed_previous_letter == 'X':
                    result += 30 if letter == 'L' else 80
                else:
                    result += 50 if letter == 'L' else 100
            elif letter == 'D' or letter == 'M':
                if processed_previous_letter == 'C':
                    result += 300 if letter == 'D' else 800
                else:
                    result += 500 if letter == 'D' else 1000
            processed_previous_letter = letter
        return result


print(Solution.roman_to_int('I'))
# 1
print(Solution.roman_to_int('VII'))
# 7
print(Solution.roman_to_int('VIII'))
# 8
print(Solution.roman_to_int('IX'))
# 9
print(Solution.roman_to_int('XC'))
# 90
print(Solution.roman_to_int('C'))
# 100
print(Solution.roman_to_int('CD'))
# 400
print(Solution.roman_to_int('MCMIV'))
# 1904
print(Solution.roman_to_int('MCMX'))
# 1910
print(Solution.roman_to_int('MMMCMXCIX'))
# 3999
