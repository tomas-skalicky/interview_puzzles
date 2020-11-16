# Task:
#
# Given a list of numbers and a target number n, find 3 numbers in the list that sums closest to the target number n.
# There may be multiple ways of creating the sum closest to the target number, you can return any combination
# in any order.
#
# Here's an example and some starter code.
#
# def closest_3sum(nums, target):
#   # Fill this in.
#
# print(closest_3sum([2, 1, -5, 4], -1))
# # Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
# # print [-5, 1, 2]
from bisect import bisect_left
from typing import List, Optional, Set


def find_3_numbers_in_list_having_sum_closest_to_target_number(numbers: List[int], target_sum: int) -> Set[int]:
    """Time complexity ... O(n ^ 2 * log n) where *n* is the length of the input List *numbers*. Reason: n ^ 2 is for
    two nested for-loops. log n is for a binary search.
    """

    number_count: int = len(numbers)
    if number_count < 3:
        raise RuntimeError('The input list contains less numbers [{}] than required 3.'.format(number_count))
    else:
        sorted_numbers: List[int] = sorted(numbers)
        triple_with_closest_sum: Optional[Set[int]] = None
        difference_of_closest_triple: Optional[int] = None

        for i in range(0, number_count - 2):
            first_number: int = sorted_numbers[i]
            for j in range(i + 1, number_count - 1):
                second_number: int = sorted_numbers[j]

                searched_third_number: int = target_sum - first_number - second_number
                candidate_index: int = bisect_left(sorted_numbers, searched_third_number, j + 1, number_count)

                if candidate_index > number_count and sorted_numbers[candidate_index] == searched_third_number:
                    return {first_number, second_number, searched_third_number}
                else:
                    if candidate_index - 1 > j:
                        smaller_number: int = sorted_numbers[candidate_index - 1]
                        left_difference: int = abs(searched_third_number - smaller_number)
                        if difference_of_closest_triple is None or left_difference < difference_of_closest_triple:
                            difference_of_closest_triple = left_difference
                            triple_with_closest_sum = {first_number, second_number, smaller_number}

                    if candidate_index < number_count:
                        greater_number: int = sorted_numbers[candidate_index]
                        right_difference: int = greater_number - searched_third_number
                        if difference_of_closest_triple is None or right_difference < difference_of_closest_triple:
                            difference_of_closest_triple = right_difference
                            triple_with_closest_sum = {first_number, second_number, greater_number}
        return triple_with_closest_sum
