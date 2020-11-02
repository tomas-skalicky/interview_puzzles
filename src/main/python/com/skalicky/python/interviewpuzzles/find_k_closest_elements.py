# Task:
#
# Given a list of sorted numbers, and two integers k and x, find k closest numbers to the pivot x.
#
# Here's an example and some starter code:
#
# def closest_nums(nums, k, x):
#  # Fill this in.
from typing import List, Dict


def closest_nums(nums: List[int], k: int, x: int) -> List[int]:
    if len(nums) < k:
        raise RuntimeError('There is not enough elements in {} to return {} elements.'.format(nums, k))
    else:
        number_lists_by_distances: Dict[int, List[int]] = {}
        distances: List[int] = []
        for number in nums:
            distance: int = abs(x - number)
            if distances.__contains__(distance):
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
