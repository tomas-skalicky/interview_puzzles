# Task:
#
# Given a list of numbers, and a target number n, find all unique combinations of a, b, c, d, such that
# a + b + c + d = n.
#
# Here's some examples and some starting code.
#
# def fourSum(nums, target):
#   # Fill this in.
#
# print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# # print {(-1, -1, 1, 1), (-2, 0, 1, 1)}
#
# print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# # print {(-5, -1, 3, 4)}
#
# print(fourSum([0, 0, 0, 0, 0], 0))
# # print {(0, 0, 0, 0)}
from typing import Dict, List, Set, Tuple


def find_4_numbers_in_list_having_target_sum(input_numbers: List[int], target_sum: int) -> Set[
    Tuple[int, int, int, int]]:
    # Time complexity ... O(n log n) where n is the length of the input list of numbers
    sorted_numbers: List[int] = sorted(input_numbers)
    number_count: int = len(sorted_numbers)

    last_indices_by_numbers: Dict[int, int] = {}
    # Time complexity in usual case (number of collisions independent of n) ... O(n) where n is the length of the input
    # list of numbers.
    # Time complexity in worst case (number of collisions dependent on n) ... O(n ^ 2)
    for i in range(0, number_count):
        current: int = sorted_numbers[i]
        last_indices_by_numbers[current] = i

    solutions: Set[Tuple[int, int, int, int]] = set()
    # Time complexity in usual case (number of collisions independent of n) ... O(n ^ 3) where n is the length of
    # the input list of numbers.
    # Time complexity in worst case (number of collisions dependent on n) ... OO(n ^ 4)
    for i in range(0, number_count - 3):
        first_number: int = sorted_numbers[i]
        for j in range(i + 1, number_count - 2):
            second_number: int = sorted_numbers[j]
            for k in range(j + 1, number_count - 1):
                third_number: int = sorted_numbers[k]
                searched_forth_number: int = target_sum - first_number - second_number - third_number
                if searched_forth_number in last_indices_by_numbers and last_indices_by_numbers[
                    searched_forth_number] > k:
                    solutions.add((first_number, second_number, third_number, searched_forth_number))

    return solutions
