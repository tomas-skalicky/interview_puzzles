# Task:
#
# Given a list of sorted numbers, and two integers k and x, find k closest numbers to the pivot x.
#
# Here's an example and some starter code:
#
# def closest_nums(nums, k, x):
#  # Fill this in.
from typing import List, Dict


def find_k_closest_elements_to_pivot(input_numbers: List[int], k: int, pivot: int) -> List[int]:
    """Time complexity ... maximum of O(n) and O(d log d) where *n* is a size of input list of numbers and *d* is
     the number of different distances
    """

    if len(input_numbers) < k:
        raise RuntimeError('There is not enough input numbers in {} to return {} elements.'.format(input_numbers, k))
    else:
        number_lists_by_distances: Dict[int, List[int]] = {}
        distances: List[int] = []
        for number in input_numbers:
            distance: int = abs(pivot - number)
            if distance in distances:
                number_lists_by_distances[distance].append(number)
            else:
                distances.append(distance)
                number_lists_by_distances[distance] = [number]

        sorted_distances: List[int] = sorted(distances)
        selected_numbers: List[int] = []
        for distance in sorted_distances:
            numbers_in_distance: List[int] = number_lists_by_distances[distance]
            sublist_size: int = min(k - len(selected_numbers), len(numbers_in_distance))
            selected_numbers += numbers_in_distance[0:sublist_size]
            if len(selected_numbers) == k:
                return selected_numbers
        raise RuntimeError('Unreachable code')
