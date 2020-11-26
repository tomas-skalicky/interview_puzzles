# Task:
#
# Given a list of numbers and a target number, find all possible unique subsets of the list of numbers that sum up to
# the target number. The numbers will all be positive numbers.
#
# Here's an example and some starter code.
#
# def sum_combinations(nums, target):
#   # Fill this in.
#
# print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# # {(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)}
from typing import List, Optional, Set, Tuple


def find_any_numbers_in_list_having_target_sum(numbers: List[int], target_sum: int) -> Set[Tuple[int, ...]]:
    """Time complexity ... O(2 ^ n) where *n* is the length of the input list *numbers*
    """

    sorted_numbers: List[int] = sorted(numbers)

    result_tuples: Set[Tuple[int, ...]] = set()
    candidate_sum_and_tuples: List[Tuple[int, List[int]]] = [(0, [])]
    for current_number in sorted_numbers:
        new_candidate_sum_and_tuples: List[Tuple[int, Optional[List[int]]]] = []
        for current_candidate_tuple_sum, current_candidate_mutable_tuple in candidate_sum_and_tuples:
            new_sum: int = current_candidate_tuple_sum + current_number
            if new_sum == target_sum:
                current_candidate_mutable_tuple.append(current_number)
                result_tuples.add(tuple(current_candidate_mutable_tuple))

            elif new_sum < target_sum:
                # Next IF conditions uses the fact that sorted_numbers are sorted ascendingly.
                if current_candidate_tuple_sum + 2 * current_number <= target_sum:
                    copied_current_candidate_mutable_tuple: List[int] = current_candidate_mutable_tuple.copy()
                    copied_current_candidate_mutable_tuple.append(current_number)
                    new_candidate_sum_and_tuples.append((new_sum, copied_current_candidate_mutable_tuple))
                if current_candidate_tuple_sum + current_number + 1 <= target_sum:
                    new_candidate_sum_and_tuples.append((current_candidate_tuple_sum, current_candidate_mutable_tuple))
        candidate_sum_and_tuples = new_candidate_sum_and_tuples
    return result_tuples
