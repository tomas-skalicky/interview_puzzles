# Task:
#
# Given a positive integer, find the square root of the integer without using any built in square root or power
# functions (math.sqrt or the ** operator). Give accuracy up to 3 decimal points.
#
# Here's an example and some starter code:
#
# def sqrt(x):
#   # Fill this in.
#
# print(sqrt(5))
# # 2.236
from typing import List, Tuple

LIST_9_0: List[int] = [i for i in reversed(range(0, 10))]


def find_greatest_lower_or_equal_number(target_number: int, adjusted_overflow: int) -> int:
    for n in LIST_9_0:
        if (adjusted_overflow + n) * n <= target_number:
            return n
    raise RuntimeError(
        'Unreachable code. Input target_number={} and adjusted_overflow={}'.format(target_number, adjusted_overflow))


def calculate_square_root(x_string: str, overflow: int, rest_from_previous_iteration: int) -> Tuple[str, int, int]:
    x_length: int = len(x_string)
    digit_blocks: List[str] = []

    start_index: int = 0
    if x_length % 2 == 1:
        digit_blocks.append(x_string[0:1])
        start_index = 1
    for i in range(start_index, x_length, 2):
        digit_blocks.append(x_string[i:i + 2])

    result: str = ''
    for current_digit_block in digit_blocks:
        adjusted_overflow: int = overflow * 10
        current_target_number: int = rest_from_previous_iteration * 100 + int(current_digit_block)
        greatest_lower_or_equal_number: int = find_greatest_lower_or_equal_number(current_target_number,
                                                                                  adjusted_overflow)
        result += str(greatest_lower_or_equal_number)
        overflow = adjusted_overflow + 2 * greatest_lower_or_equal_number
        rest_from_previous_iteration = current_target_number - (
                adjusted_overflow + greatest_lower_or_equal_number) * greatest_lower_or_equal_number
        if rest_from_previous_iteration == 0:
            break

    return result, overflow, rest_from_previous_iteration


# Using a long division technique. See https://www.youtube.com/watch?v=Ga1_wuLz0QM
def manual_square_root(x: int) -> float:
    result, overflow, rest_from_previous_iteration = calculate_square_root(str(x), 0, 0)
    if rest_from_previous_iteration > 0:
        result_decimal, overflow, rest_from_previous_iteration = calculate_square_root('00' * 3, overflow,
                                                                                       rest_from_previous_iteration)
        return float('{}.{}'.format(result, result_decimal))
    else:
        return int(result)
