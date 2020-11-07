# Task:
#
# Given a non-negative integer n, convert the integer to hexadecimal and return the result as a string. Hexadecimal is
# a base 16 representation of a number, where the digits are 0123456789ABCDEF. Do not use any builtin base conversion
# functions like hex.
#
# Here's an example and some starter code.
#
# def to_hex(n):
#   # Fill this in.

BASE: int = 16


def convert_decimal_digit_to_hexadecimal_digit(decimal: int) -> str:
    if decimal < 10:
        return str(decimal)
    elif decimal == 10:
        return 'A'
    elif decimal == 11:
        return 'B'
    elif decimal == 12:
        return 'C'
    elif decimal == 13:
        return 'D'
    elif decimal == 14:
        return 'E'
    else:
        return 'F'


def convert_decimal_to_hexadecimal_without_builtin_functions(decimal: int) -> str:
    if decimal == 0:
        return '0'
    else:
        result_string: str = ''
        rest: int = decimal
        negative: bool = False
        if decimal < 0:
            rest *= -1
            negative = True
        while rest != 0:
            next_digit: int = rest % BASE
            rest = int(rest / BASE)
            result_string = convert_decimal_digit_to_hexadecimal_digit(next_digit) + result_string
        return '-{}'.format(result_string) if negative else result_string
