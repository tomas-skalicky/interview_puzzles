# Task:
#
# Given a string, convert it to an integer without using the builtin str function. You are allowed to use ord to convert
# a character to ASCII code.
#
# Consider all possible cases of an integer. In the case where the string is not a valid integer, return None.
#
# Here's some starting code:
#
# def convert_to_int(s):
#   # Fill this in.
#
# print(convert_to_int('-105') + 1)
# # -104
from typing import List, Optional

MINUS_ORDINAL: int = 45
ZERO_ORDINAL: int = 48
NINE_ORDINAL: int = ZERO_ORDINAL + 9


def convert_string_to_integer_with_ord_function(input_string: str) -> Optional[int]:
    result: Optional[int] = None
    characters: List[str] = list(input_string)
    negative: bool = False
    for i in range(0, len(characters)):
        character: str = characters[i]
        ordinal_value: int = ord(character)
        if ZERO_ORDINAL <= ordinal_value <= NINE_ORDINAL:
            current_number: int = ordinal_value - ZERO_ORDINAL
            result = result * 10 + current_number if result is not None else current_number
        elif ordinal_value == MINUS_ORDINAL and i == 0:
            negative = True
        else:
            return None
    return result * (-1 if negative else 1)
