# Task:
#
# You are only allowed to perform 2 operations, multiply a number by 2, or subtract a number by 1. Given a number x and
# a number y, find the minimum number of operations needed to go from x to y.
#
# Here's an example and some starter code.
#
# def min_operations(x, y):
#   # Fill this in.
#
# print(min_operations(6, 20))
# # (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
# # print 3
from collections import deque
from typing import Deque, Tuple, Set


def find_minimum_number_of_operations_to_reach_target_number(start: int, target: int) -> int:
    if start < target < 0:
        raise RuntimeError(
            'There is no way how we can get {} from {} applying operations "-1" and "*2".'.format(target, start))
    elif start >= 0 and target < 0:
        return start - target
    elif start == target:
        return 0
    else:
        already_processed_numbers: Set[int] = set()
        numbers_to_process_and_min_steps_to_reach: Deque[Tuple[int, int]] = deque()
        numbers_to_process_and_min_steps_to_reach.append((start, 0))
        while True:
            number_to_process, min_steps_to_reach = numbers_to_process_and_min_steps_to_reach.popleft()
            if number_to_process == target:
                return min_steps_to_reach
            elif number_to_process in already_processed_numbers:
                pass
            else:
                already_processed_numbers.add(number_to_process)
                numbers_to_process_and_min_steps_to_reach.append((number_to_process * 2, min_steps_to_reach + 1))
                numbers_to_process_and_min_steps_to_reach.append((number_to_process - 1, min_steps_to_reach + 1))
