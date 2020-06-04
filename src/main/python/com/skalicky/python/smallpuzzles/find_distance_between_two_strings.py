# Task:
#
# Given two strings, determine the edit distance between them. The edit distance is defined as the minimum
# number of edits (insertion, deletion, or substitution) needed to change one string to the other.
#
# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).
#
# Here's the signature:
#
# def distance(s1, s2):
#   # Fill this in.
#
# print distance('biting', 'sitting')
# # 2


from typing import Dict, Any


# Time complexity O(3^max(len(s1), len(s2))) because the algorithm evaluates the complete tree of possibilities.
# Space complexity O(3^max(len(s1), len(s2))) due to the call stack.
# More details on https://www.geeksforgeeks.org/edit-distance-dp-5/
def distance_with_recursion(s1: str, s2: str):
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0:1] == s2[0:1]:
        return distance_with_recursion(s1[1:], s2[1:])
    return 1 + min(distance_with_recursion(s1[1:], s2[1:]),
                   distance_with_recursion(s1, s2[1:]),
                   distance_with_recursion(s1[1:], s2))


interim_results_for_recursion_with_optimization: Dict[Any, int] = {}


# Time complexity O(m * n) because the algorithm prunes those branches of tree of possibilities which the algorithm
# already knows a distance (=interim result) for.
# Space complexity O(m * n) due to the call stack as well as due to the dictionary of interim results.
def distance_with_recursion_with_optimization(s1: str, s2: str):
    interim_results_key = (s1, s2)
    if interim_results_for_recursion_with_optimization.__contains__(interim_results_key):
        return interim_results_for_recursion_with_optimization[interim_results_key]

    distance: int
    if s1 == s2:
        distance = 0
    elif len(s1) == 0:
        distance = len(s2)
    elif len(s2) == 0:
        distance = len(s1)
    elif s1[0:1] == s2[0:1]:
        distance = distance_with_recursion_with_optimization(s1[1:], s2[1:])
    else:
        distance = 1 + min(distance_with_recursion_with_optimization(s1[1:], s2[1:]),
                           distance_with_recursion_with_optimization(s1, s2[1:]),
                           distance_with_recursion_with_optimization(s1[1:], s2))
    interim_results_for_recursion_with_optimization[interim_results_key] = distance
    return distance


# Time complexity O(m * n)
# Space complexity O(m * n)
# More details on https://www.geeksforgeeks.org/edit-distance-dp-5/
def distance_with_dynamic_programming(s1: str, s2: str):
    if s1 == s2:
        return 0
    elif len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    else:
        interim_results: Dict[Any, int] = {(0, 0): 0}
        for i in range(1, len(s1) + 1):
            interim_results[(i, 0)] = i - 1
        for j in range(1, len(s2) + 1):
            interim_results[(0, j)] = j - 1
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1:i] == s2[j - 1:j]:
                    interim_results[(i, j)] = interim_results[(i - 1, j - 1)]
                else:
                    interim_results[(i, j)] = 1 + min(
                        interim_results[(i - 1, j - 1)],
                        interim_results[(i - 1, j)],
                        interim_results[(i, j - 1)]
                    )
        return interim_results[(len(s1), len(s2))]


# Time complexity O(m * n)
# Space complexity O(m) because we need only the previous and the current row.
# More details on https://www.geeksforgeeks.org/edit-distance-dp-5/
def distance_with_spacial_optimized_dynamic_programming(s1: str, s2: str):
    if s1 == s2:
        return 0
    elif len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    else:
        interim_results: Dict[Any, int] = {(0, 0): 0, (1, 0): 1}
        for j in range(1, len(s2) + 1):
            interim_results[(0, j)] = j - 1
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1:i] == s2[j - 1:j]:
                    interim_results[(i % 2, j)] = interim_results[((i - 1) % 2, j - 1)]
                else:
                    interim_results[(i % 2, j)] = 1 + min(
                        interim_results[((i - 1) % 2, j - 1)],
                        interim_results[((i - 1) % 2, j)],
                        interim_results[(i % 2, j - 1)]
                    )
        return interim_results[(len(s1) % 2, len(s2))]


def calculate_distance_by_all_ways(s1: str, s2: str, expected_result: int):
    print("s1={}, s2={}, expected_result={}".format(s1, s2, expected_result))

    actual_result = distance_with_recursion(s1, s2)
    if actual_result == expected_result:
        print(" - recursion: OK")
    else:
        print(" - recursion: ERROR, actual_result={}".format(actual_result))

    global interim_results_for_recursion_with_optimization
    interim_results_for_recursion_with_optimization.clear()
    actual_result = distance_with_recursion_with_optimization(s1, s2)
    if actual_result == expected_result:
        print(" - recursion with optimization: OK")
    else:
        print(" - recursion with optimization: ERROR, actual_result={}".format(actual_result))

    actual_result = distance_with_dynamic_programming(s1, s2)
    if actual_result == expected_result:
        print(" - dynamic programming: OK")
    else:
        print(" - dynamic programming: ERROR, actual_result={}".format(actual_result))

    actual_result = distance_with_spacial_optimized_dynamic_programming(s1, s2)
    if actual_result == expected_result:
        print(" - dynamic programming with optimized space complexity: OK")
    else:
        print(" - dynamic programming with optimized space complexity: ERROR, actual_result={}".format(actual_result))
    print()


calculate_distance_by_all_ways('sitting', 'sitting', 0)
calculate_distance_by_all_ways('biting', 'sitting', 2)
calculate_distance_by_all_ways('geek', 'gesek', 1)
calculate_distance_by_all_ways('cat', 'cut', 1)
calculate_distance_by_all_ways('sunday', 'saturday', 3)
calculate_distance_by_all_ways('cat', '', 3)
calculate_distance_by_all_ways('', 'cut', 3)
