# Task:
#
# You have a landscape, in which puddles can form. You are given an array of non-negative integers representing
# the elevation at each location. Return the amount of water that would accumulate if it rains.
#
# For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#        X
#    X███XX█X
#  X█XX█XXXXXX
# # [0,1,0,2,1,0,1,3,2,1,2,1]
# Here's your starting pont:
#
# def capacity(arr):
#   # Fill this in.
#
# print capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# # 6
from collections import deque
from typing import Deque, List, Tuple


def identify_bottom_of_puddle(initial_elevation_index: int,
                              landscape: List[int],
                              bottoms_of_puddles_to_process: Deque[Tuple]) -> int:
    landscape_length: int = len(landscape)
    initial_elevation = landscape[initial_elevation_index]

    candidate_elevation_index_for_start: int = initial_elevation_index
    while candidate_elevation_index_for_start > 0 and landscape[
        candidate_elevation_index_for_start] == initial_elevation:
        candidate_elevation_index_for_start -= 1

    if landscape[candidate_elevation_index_for_start] > initial_elevation:
        puddle_bottom_start_index: int = candidate_elevation_index_for_start + 1

        candidate_elevation_index_for_end: int = initial_elevation_index
        while candidate_elevation_index_for_end < landscape_length - 1 and landscape[
            candidate_elevation_index_for_end] == initial_elevation:
            candidate_elevation_index_for_end += 1

        if landscape[candidate_elevation_index_for_end] > initial_elevation:
            bottoms_of_puddles_to_process.append((puddle_bottom_start_index, candidate_elevation_index_for_end - 1))
            return candidate_elevation_index_for_end + 1
        else:
            return candidate_elevation_index_for_end
    else:
        return initial_elevation_index + 1


def calculate_rainwater_in_puddles(input_landscape: List[int]) -> int:
    """Time complexity ... O(n ^ 2) where *n* is the length of the input List
    """

    # We create a copy of input List because we modify the List in the method.
    landscape: List[int] = input_landscape.copy()
    landscape_length: int = len(landscape)
    if landscape_length < 3:
        return 0
    else:
        total_rainwater: int = 0
        bottoms_of_puddles_to_process: Deque[Tuple[int, int]] = deque()
        current_elevation_index: int = 1
        # O(n) where n is the length of the input list because each element of the list is visited at most twice
        while current_elevation_index < landscape_length - 1:
            current_elevation_index = identify_bottom_of_puddle(current_elevation_index, landscape,
                                                                bottoms_of_puddles_to_process)

        while len(bottoms_of_puddles_to_process) > 0:
            puddle_bottom_start_index, puddle_bottom_end_index = bottoms_of_puddles_to_process.popleft()
            sides_min_elevation: int = min(landscape[puddle_bottom_start_index - 1],
                                           landscape[puddle_bottom_end_index + 1])
            bottom_elevation: int = landscape[puddle_bottom_start_index]
            elevation_difference: int = sides_min_elevation - bottom_elevation
            for elevation_index in range(puddle_bottom_start_index, puddle_bottom_end_index + 1):
                total_rainwater += elevation_difference
                landscape[elevation_index] = sides_min_elevation
            identify_bottom_of_puddle(puddle_bottom_start_index - 1, landscape, bottoms_of_puddles_to_process)
        return total_rainwater
