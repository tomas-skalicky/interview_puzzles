# Task:
#
# Given a string s and a character c, find the distance for all characters in the string to the character c in
# the string s. You can assume that the character c will appear at least once in the string.
#
# Here's an example and some starter code:
#
# def shortest_dist(s, c):
#   # Fill this in.
#
# print(shortest_dist('helloworld', 'l'))
# # [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
from typing import List


def calculate_distances_in_one_direction(input_string: str, target_character: str, distances: List[int],
                                         input_range: iter):
    distance_to_closest: int = len(input_string)
    for i in input_range:
        current_character: str = input_string[i]
        if current_character == target_character:
            distance_to_closest = 0
            distances[i] = 0
        else:
            distance_to_closest += 1
            distances[i] = min(distances[i], distance_to_closest)


def find_shortest_distance_of_characters_to_given_character(input_string: str, target_character: str) -> List[int]:
    """Time complexity ... O(n) where *n* is the length of the *input_string*. Reason: we iterate twice over all
    characters of *input_string*.
    """

    string_length: int = len(input_string)
    distances: List[int] = [string_length] * string_length
    calculate_distances_in_one_direction(input_string, target_character, distances, range(0, string_length))
    calculate_distances_in_one_direction(input_string, target_character, distances, reversed(range(0, string_length)))
    return distances
