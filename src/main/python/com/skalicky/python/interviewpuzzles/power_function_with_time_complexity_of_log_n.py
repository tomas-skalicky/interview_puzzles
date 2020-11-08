# Task:
#
# The power function calculates x raised to the nth power. If implemented in O(n) it would simply be a for loop over n
# and multiply x n times. Instead implement this power function in O(log n) time. You can assume that n will be
# a non-negative integer.
#
# Here's some starting code:
#
# def pow(x, n):
#   # Fill this in.
#
# print(pow(5, 3))
# # 125
from typing import Dict


def power_function_with_time_complexity_of_log_n(base, exponent: int):
    if exponent == 0:
        return 1
    else:
        powers: Dict[int,] = {}
        current_exponent: int = 1
        powers[current_exponent] = base
        while exponent - current_exponent * 2 >= 0:
            powers[current_exponent * 2] = powers[current_exponent] * powers[current_exponent]
            current_exponent = current_exponent * 2
        remaining_exponent: int = exponent
        result = 1
        while current_exponent >= 0:
            if remaining_exponent == current_exponent:
                return result * powers[current_exponent]
            elif remaining_exponent > current_exponent:
                result *= powers[current_exponent]
                remaining_exponent -= current_exponent
            current_exponent /= 2
        raise RuntimeError('Unreachable code')
