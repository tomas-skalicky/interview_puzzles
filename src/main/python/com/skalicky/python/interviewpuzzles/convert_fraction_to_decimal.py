# Task:
#
# Given a numerator and a denominator, find what the equivalent decimal representation is as a string. If the decimal
# representation has recurring digits, then put those digits in brackets (ie 4/3 should be represented by 1.(3) to
# represent 1.333...). Do not use any built in evaluator functions like python's eval. You can also assume that
# the denominator will be nonzero.
#
# Here's some examples and some starter code:
#
# def frac_to_dec(numerator, denominator):
#   # Fill this in.
#
# print(frac_to_dec(-3, 2))
# # -1.5
#
# print(frac_to_dec(4, 3))
# # 1.(3)
#
# print(frac_to_dec(1, 6))
# # 0.1(6)
from typing import Dict


def convert_fraction_to_decimal(numerator: int, denominator: int) -> str:
    result_string: str = ''
    rest: int = numerator
    first_iteration: bool = True
    indices_when_rests_calculated_by_rests_after_decimal_comma: Dict[int, int] = {}
    while True:
        partial_result: int = int(rest / denominator)
        result_string += str(partial_result)
        rest = abs(rest - denominator * partial_result)
        if rest != 0:
            if first_iteration:
                result_string += '.'
                indices_when_rests_calculated_by_rests_after_decimal_comma[rest] = len(result_string)
                first_iteration = False
            else:
                if rest in indices_when_rests_calculated_by_rests_after_decimal_comma:
                    position: int = indices_when_rests_calculated_by_rests_after_decimal_comma[rest]
                    return '{}({})'.format(result_string[:position], result_string[position:])
                else:
                    indices_when_rests_calculated_by_rests_after_decimal_comma[rest] = len(result_string)
            rest *= 10
        else:
            return result_string
