# Task:
#
# Given an integer, convert the integer to a roman numeral. You can assume the input will be between 1 to 3999.
#
# The rules for roman numerals are as following:
#
# There are 7 symbols, which correspond to the following values.
# I   1
# V   5
# X   10
# L   50
# C   100
# D   500
# M   1000
# The value of a roman numeral are the digits added together. For example the roman numeral 'XX' is
# V + V = 10 + 10 = 20. Typically the digits are listed from largest to smallest, so X should always come before I.
# Thus the largest possible digits should be used first before the smaller digits (so to represent 50, instead of XXXXX,
# we should use L).
#
# There are a couple special exceptions to the above rule.
#
# To represent 4, we should use IV instead of IIII. Notice that I comes before V.
# To represent 9, we should use IX instead of VIIII.
# To represent 40, we should use XL instead of XXXX.
# To represent 90, we should use XC instead of LXXXX.
# To represent 400, we should use CD instead of CCCC.
# To represent 900, we should use CM instead of DCCCC.
#
# Here are some examples and some starter code.
#
# def integer_to_roman(num):
#   # Fill this in.
#
# print(integer_to_roman(1000))
# # M
# print(integer_to_roman(48))
# # XLVIII
# print(integer_to_roman(444))
# # CDXLIV
from math import floor


def convert_decimal_to_roman(input_number: int) -> str:
    result_roman: str = ''
    rest: int = input_number
    if rest >= 1000:
        thousands: int = floor(rest / 1000)
        result_roman += 'M' * thousands
        rest -= thousands * 1000

    if rest >= 900:
        result_roman += 'CM'
        rest -= 900
    elif 500 > rest >= 400:
        result_roman += 'CD'
        rest -= 400
    else:
        if rest >= 500:
            result_roman += 'D'
            rest -= 500
        if rest >= 100:
            hundreds: int = floor(rest / 100)
            result_roman += 'C' * hundreds
            rest -= hundreds * 100

    if rest >= 90:
        result_roman += 'XC'
        rest -= 90
    elif 50 > rest >= 40:
        result_roman += 'XL'
        rest -= 40
    else:
        if rest >= 50:
            result_roman += 'L'
            rest -= 50
        if rest >= 10:
            tens: int = floor(rest / 10)
            result_roman += 'X' * tens
            rest -= tens * 10

    if rest == 9:
        return result_roman + 'IX'
    elif rest == 4:
        return result_roman + 'IV'
    else:
        if rest >= 5:
            result_roman += 'V'
            rest -= 5
        if rest >= 1:
            result_roman += 'I' * rest
        return result_roman
