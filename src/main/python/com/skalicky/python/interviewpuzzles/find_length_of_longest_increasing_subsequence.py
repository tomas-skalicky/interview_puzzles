# Task:
#
# You are given an array of integers. Return the length of the longest increasing subsequence (not necessarily
# contiguous) in the array.
#
# Example:
# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#
# The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
from typing import List, Dict


def add_new_candidate_to_dictionary_if_suitable(candidate: List[int], candidates_by_length: Dict[int, List[int]]):
    current_candidate_new_length: int = len(candidate)
    index_of_last: int = current_candidate_new_length - 1
    if not candidates_by_length.__contains__(current_candidate_new_length) or \
            candidates_by_length[current_candidate_new_length][index_of_last] > candidate[index_of_last]:
        candidates_by_length[current_candidate_new_length] = candidate


# Trivial algorithm would have a time complexity of O (2 ^ n) where n is a size of input list.
# This one has a time complexity of O (n * min(n, len(longest_subsequence))) which is in the worst case O (n ^ 2)
def find_longest_increasing_subsequence(numbers: List[int]):
    if len(numbers) == 0:
        return []
    else:
        candidates_by_lengths: Dict[int, List[int]] = dict()
        for number in numbers:
            new_candidates_by_lengths: Dict[int, List[int]] = dict()
            add_new_candidate_to_dictionary_if_suitable([number], new_candidates_by_lengths)
            for candidate_length in candidates_by_lengths.keys():
                candidate: List[int] = candidates_by_lengths[candidate_length]
                add_new_candidate_to_dictionary_if_suitable(candidate, new_candidates_by_lengths)
                index_of_last: int = len(candidate) - 1
                if candidate[index_of_last] < number:
                    new_longer_candidate: List[int] = list(candidate)
                    new_longer_candidate.append(number)
                    add_new_candidate_to_dictionary_if_suitable(new_longer_candidate, new_candidates_by_lengths)
                elif candidate[index_of_last - 1] < number < candidate[index_of_last]:
                    new_candidate_with_last_replaced: List[int] = list(candidate)
                    new_candidate_with_last_replaced[index_of_last] = number
                    add_new_candidate_to_dictionary_if_suitable(new_candidate_with_last_replaced,
                                                                new_candidates_by_lengths)
            candidates_by_lengths = new_candidates_by_lengths
        return candidates_by_lengths[max(candidates_by_lengths.keys())]


def print_result(result_list: List[int]):
    print('{} -> length of {}'.format(result_list, len(result_list)))


print_result(find_longest_increasing_subsequence([]))
# [] -> length of 0
print_result(find_longest_increasing_subsequence([2, 0, 9, -1, 8, 4, 2, 3]))
# [-1, 2, 3] -> length of 3
print_result(find_longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
# [0, 2, 6, 9, 11, 15] -> length of 6
