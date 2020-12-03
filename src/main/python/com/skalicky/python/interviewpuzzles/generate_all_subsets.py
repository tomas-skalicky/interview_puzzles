# Task:
#
# Given a list of unique numbers, generate all possible subsets without duplicates. This includes the empty set as well.
#
# Here's an example and some starter code.
#
# def generate_all_subsets(numbers):
#     # Fill this in.
#
# print(generate_all_subsets([1, 2, 3]))
# # [{}, {3}, {2}, {2, 3}, {1}, {1, 3}, {1, 2}, {1, 2, 3}]
from typing import List, Set


def generate_all_subsets(numbers: List[int]) -> List[Set[int]]:
    """Efficiency ... the implemented algorithm visits each element in the result List of Sets twice, once in the first
    while-loop, the second time in the for-loop converting indices to elements.
    """

    number_count: int = len(numbers)

    all_subsets_of_indices: List[List[int]] = [[]]
    subsets_of_indices_from_previous_iteration: List[List[int]] = all_subsets_of_indices
    while len(subsets_of_indices_from_previous_iteration) > 1 or len(
            subsets_of_indices_from_previous_iteration[0]) != number_count:
        subsets_of_indices_from_current_iteration: List[List[int]] = []

        for subset_of_indices in subsets_of_indices_from_previous_iteration:
            subset_size: int = len(subset_of_indices)
            last_index_in_subset: int = subset_of_indices[subset_size - 1] if subset_size > 0 else -1
            for i in range(last_index_in_subset + 1, number_count):
                new_subset_of_indices: List[int] = subset_of_indices.copy()
                new_subset_of_indices.append(i)
                subsets_of_indices_from_current_iteration.append(new_subset_of_indices)

        all_subsets_of_indices.extend(subsets_of_indices_from_current_iteration)
        subsets_of_indices_from_previous_iteration = subsets_of_indices_from_current_iteration

    all_subsets_of_elements: List[Set[int]] = []
    for subset_of_indices in all_subsets_of_indices:
        new_subset: Set[int] = set()
        for index in subset_of_indices:
            new_subset.add(numbers[index])
        all_subsets_of_elements.append(new_subset)

    return all_subsets_of_elements
