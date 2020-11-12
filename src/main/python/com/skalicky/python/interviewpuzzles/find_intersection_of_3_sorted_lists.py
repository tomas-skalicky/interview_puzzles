# Task:
#
# Given 3 sorted lists, find the intersection of those 3 lists.
#
# Here's an example and some starter code.
#
# def intersection(list1, list2, list3):
#   # Fill this in.
#
# print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# # [4]
from typing import List


def find_intersection_of_3_sorted_lists(list1: List[object], list2: List[object], list3: List[object]) -> List[object]:
    """Time complexity ... O(n) where *n* is the length of the longest input list. Reason: we are vising each element
    in each input list only constant number of times.
    """

    list1_length: int = len(list1)
    list2_length: int = len(list2)
    list3_length: int = len(list3)
    if list1_length == list2_length == list3_length == 0:
        return []
    else:
        result: List[object] = []
        list1_index: int = 0
        list2_index: int = 0
        list3_index: int = 0
        while list1_index < list1_length and list2_index < list2_length and list3_index < list3_length:
            if list1[list1_index] == list2[list2_index] == list3[list3_index]:
                result.append(list1[list1_index])
                list1_index += 1
                list2_index += 1
                list3_index += 1
            elif list1[list1_index] > list2[list2_index]:
                list2_index += 1
            elif list1[list1_index] > list3[list3_index]:
                list3_index += 1
            elif list2[list2_index] > list1[list1_index]:
                list1_index += 1
            elif list2[list2_index] > list3[list3_index]:
                list3_index += 1
            elif list3[list3_index] > list1[list1_index]:
                list1_index += 1
            elif list3[list3_index] > list2[list2_index]:
                list2_index += 1
            else:
                raise RuntimeError(
                    'Unreachable code: list1_index={}, list2_index={}, list3_index={}'.format(list1_index, list2_index,
                                                                                              list3_index))
        return result
