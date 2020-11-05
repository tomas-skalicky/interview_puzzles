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


def frac_to_dec(numerator: int, denominator: int) -> str:
    result_str: str = ''
    rest: int = numerator
    first_iteration: bool = True
    existing_rests_after_decimal_comma_and_position: Dict[int, int] = {}
    while True:
        partial_result: int = int(rest / denominator)
        result_str += str(partial_result)
        rest = abs(rest - denominator * partial_result)
        if rest != 0:
            if first_iteration:
                result_str += '.'
                existing_rests_after_decimal_comma_and_position[rest] = len(result_str)
                first_iteration = False
            else:
                if existing_rests_after_decimal_comma_and_position.__contains__(rest):
                    position: int = existing_rests_after_decimal_comma_and_position[rest]
                    return '{}({})'.format(result_str[:position], result_str[position:])
                else:
                    existing_rests_after_decimal_comma_and_position[rest] = len(result_str)
            rest *= 10
        else:
            return result_str
