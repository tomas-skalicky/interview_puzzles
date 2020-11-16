# Task:
#
# Given a list of numbers, for each element find the next element that is larger than the current element. Return
# the answer as a list of indices. If there are no elements larger than the current element, then use -1 instead.
#
# Here's an example and some starter code:
#
# def larger_number(nums):
#   # Fill this in.
#
# # print [2, 2, 3, 4, -1, -1]
# print(larger_number([3, 2, 5, 6, 9, 8]))
from math import floor
from typing import Dict, List


def bisect_left_for_descendingly_sorted_list(input_list, searched_element):
    """Simplified copy of bisect.bisect_left adapted for input list sorted descendingly.
    """

    lower_bound: int = 0
    higher_bound: int = len(input_list)
    while lower_bound < higher_bound:
        middle_index: int = floor((lower_bound + higher_bound) / 2)
        if input_list[middle_index] < searched_element:
            higher_bound = middle_index
        else:
            lower_bound = middle_index + 1
    return lower_bound


def insort_left_for_descendingly_sorted_list(input_list, searched_element):
    """Simplified copy of bisect.insort_left adapted for input list sorted descendingly.
    """

    insert_index = bisect_left_for_descendingly_sorted_list(input_list, searched_element)
    input_list.insert(insert_index, searched_element)


def find_indices_of_next_larger_number(input_numbers: List[int]) -> List[int]:
    """Time complexity ... O(n log n) where *n* is a size of the input list
    """

    result_indices: List[int] = [-1 for i in range(0, len(input_numbers))]
    index_lists_by_searched_closest_larger_numbers: Dict[int, List[int]] = {}
    # Ordered descendingly since the insert and remove operation at the end of List has a time complexity of O(1).
    # The insert and remove operation at the beginning of List has however a time complexity of O(n)
    sorted_searched_closest_larger_numbers_ordered_desc: List[int] = []
    for i in range(0, len(input_numbers)):
        current_number: int = input_numbers[i]
        # Each element in the list will be processed by the inner for loop at most once.
        while len(sorted_searched_closest_larger_numbers_ordered_desc) > 0:
            searched_number: int = sorted_searched_closest_larger_numbers_ordered_desc.pop()
            if searched_number <= current_number:
                for non_processed_index in index_lists_by_searched_closest_larger_numbers.pop(searched_number):
                    result_indices[non_processed_index] = i
            else:
                sorted_searched_closest_larger_numbers_ordered_desc.append(searched_number)
                break

        searched_closest_larger_number: int = current_number + 1
        if searched_closest_larger_number in index_lists_by_searched_closest_larger_numbers:
            index_lists_by_searched_closest_larger_numbers[searched_closest_larger_number].append(i)
        else:
            # Time complexity ... O(log n)
            insort_left_for_descendingly_sorted_list(sorted_searched_closest_larger_numbers_ordered_desc,
                                                     searched_closest_larger_number)
            index_lists_by_searched_closest_larger_numbers[searched_closest_larger_number] = [i]

    return result_indices
