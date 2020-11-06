# Task:
#
# Given a non-negative integer n, convert n to base 2 in string form. Do not use any built in base 2 conversion
# functions like bin.
#
# Here's an example and some starter code:
#
# def base_2(n):
#   # Fill this in.
#
# print(base_2(123))
# # 1111011
#
#
# In the above example, 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 = 123.
from typing import Dict, List


def convert_to_binary_representation(input_number: int) -> str:
    if input_number == 0:
        return '0'
    else:
        possible_exponents_asc: List[int] = [0]
        results_by_exponents: Dict[int, int] = dict({0: 1})

        next_number: int = 1
        current_result: int = 1
        while current_result * 2 <= input_number:
            current_result *= 2
            possible_exponents_asc.append(next_number)
            results_by_exponents[next_number] = current_result
            next_number += 1

        rest: int = input_number
        binary_representation: str = ''
        while len(possible_exponents_asc) > 0:
            greatest_remaining_exponent: int = possible_exponents_asc.pop()
            greatest_remaining_result: int = results_by_exponents[greatest_remaining_exponent]
            if greatest_remaining_result <= rest:
                binary_representation += '1'
                rest -= greatest_remaining_result
            else:
                binary_representation += '0'
        return binary_representation
