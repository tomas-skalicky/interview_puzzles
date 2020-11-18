# Task:
#
# Given a string that may represent a number, determine if it is a number. Here's some of examples of how the number may
# be presented:
#
# "123" # Integer
# "12.3" # Floating point
# "-123" # Negative numbers
# "-.3" # Negative floating point
# "1.5e5" # Scientific notation
#
# Here's some examples of what isn't a proper number:
#
# "12a" # No letters
# "1 2" # No space between numbers
# "1e1.2" # Exponent can only be an integer (positive or negative or 0)
#
# Scientific notation requires the first number to be less than 10, however to simplify the solution assume the first
# number can be greater than 10. Do not parse the string with int() or any other python functions.
#
# Here's some starting code:
#
# def parse_number(s):
#    # Fill this in.
#
# print(parse_number("12.3"))
# # True
#
# print(parse_number("12a"))
# # False
from typing import Optional

DIGIT_CHARACTERS = set([str(i) for i in range(0, 10)])


def is_digit(character: str) -> bool:
    return character in DIGIT_CHARACTERS


def is_negative_sign(character: str) -> bool:
    return character == '-'


def is_exponent_sign(character: str) -> bool:
    return character == 'e'


def is_floating_sign(character: str) -> bool:
    return character == '.'


def parse_number(s: str) -> bool:
    is_negative_number: bool = False
    number_having_more_digits: bool = False
    is_float: bool = False
    has_exponent: bool = False
    has_negative_exponent: bool = False
    previous_character: Optional[str] = None

    for i in range(0, len(s)):
        character: str = s[i]
        if is_digit(character):
            if not has_exponent and not is_float and is_digit(previous_character):
                number_having_more_digits = True
        elif is_floating_sign(character):
            if has_exponent or is_float:
                return False
            else:
                is_float = True
        elif is_negative_sign(character):
            if i == 0:
                is_negative_number = True
            elif has_negative_exponent or (not has_exponent and is_negative_number):
                return False
            elif has_exponent and is_exponent_sign(previous_character):
                has_negative_exponent = True
            else:
                return False
        elif is_exponent_sign(character):
            if has_exponent or is_floating_sign(previous_character) or number_having_more_digits:
                return False
            else:
                has_exponent = True
        else:
            return False

        previous_character = character
    return True


print(parse_number("12.3"))
# True
print(parse_number("123"))
# True
print(parse_number("-123"))
# True
print(parse_number("-.3"))
# True
print(parse_number(".3"))
# True
print(parse_number("1.5e5"))
# True
print(parse_number("2e0"))
# True
print(parse_number("2e-22"))
# True

print(parse_number("12a"))
# False
print(parse_number("1 2"))
# False
print(parse_number("1e1.2"))
# False
print(parse_number("15e5"))
# False
print(parse_number("1..3"))
# False
print(parse_number("--1"))
# False
