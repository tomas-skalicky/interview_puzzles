# Task:
#
# Given a string, rearrange the string so that no character next to each other are the same. If no such arrangement is
# possible, then return None.
#
# Example:
# Input: abbccc
# Output: cbcbca
# def rearrangeString(s):
#   # Fill this in.
#
# print rearrangeString('abbccc')
# # cbcabc
from collections import deque
from typing import List, Dict, Tuple, Optional


def multiple_letter(letter: str, occurrence_count: int) -> List[str]:
    result: List[str] = []
    for i in range(0, occurrence_count):
        result.append(letter)
    return result


def rearrange_string(s: str) -> Optional[str]:
    total_length: int = len(s)
    if total_length <= 1:
        return s
    else:
        occurrence_counts_by_letters: Dict[str, int] = {}
        for letter in list(s):
            if occurrence_counts_by_letters.__contains__(letter):
                occurrence_counts_by_letters[letter] += 1
            else:
                occurrence_counts_by_letters[letter] = 1

        list_of_letters_by_occurrence_counts: Dict[int, List[str]] = {}
        for letter in occurrence_counts_by_letters.keys():
            occurrence_count: int = occurrence_counts_by_letters[letter]
            if not list_of_letters_by_occurrence_counts.__contains__(occurrence_count):
                list_of_letters_by_occurrence_counts[occurrence_count] = []
            list_of_letters_by_occurrence_counts[occurrence_count].append(letter)

        occurrence_counts_sorted_desc: List[int] = sorted(list_of_letters_by_occurrence_counts.keys(), reverse=True)
        largest_occurrence_count: int = occurrence_counts_sorted_desc[0]
        if largest_occurrence_count > total_length - largest_occurrence_count + 1:
            return None
        else:
            letters_and_occurrence_counts_sorted_desc: List[Tuple[str, int]] = []
            for occurrence_count in occurrence_counts_sorted_desc:
                for letter in list_of_letters_by_occurrence_counts[occurrence_count]:
                    letters_and_occurrence_counts_sorted_desc.append((letter, occurrence_count))

            lists_to_distribute: List[List[str]] = []
            last_non_stored_list: List[str] = []
            occurrence_total_in_last_non_stored_list: int = 0
            for letter_and_its_occurrence_count in letters_and_occurrence_counts_sorted_desc:
                current_letter: str = letter_and_its_occurrence_count[0]
                current_occurrence_count: int = letter_and_its_occurrence_count[1]
                if occurrence_total_in_last_non_stored_list + current_occurrence_count > largest_occurrence_count:
                    first_part_size: int = largest_occurrence_count - occurrence_total_in_last_non_stored_list
                    last_non_stored_list += multiple_letter(current_letter, first_part_size)
                    last_non_stored_list = []
                    second_part_size: int = current_occurrence_count - first_part_size
                    last_non_stored_list += multiple_letter(current_letter, second_part_size)
                    occurrence_total_in_last_non_stored_list = second_part_size
                else:
                    last_non_stored_list += multiple_letter(current_letter, current_occurrence_count)
                    occurrence_total_in_last_non_stored_list += current_occurrence_count
                    if occurrence_total_in_last_non_stored_list == largest_occurrence_count:
                        lists_to_distribute.append(last_non_stored_list)
                        last_non_stored_list = []
                        occurrence_total_in_last_non_stored_list = 0
            if occurrence_total_in_last_non_stored_list > 0:
                lists_to_distribute.append(last_non_stored_list)

            result_string: str = ''
            for i in range(0, largest_occurrence_count):
                for list_to_distribute in lists_to_distribute:
                    if len(list_to_distribute) > i:
                        result_string += list_to_distribute[i]
            return result_string


print(rearrange_string('a'))
# a
print(rearrange_string('abbccc'))
# cbcbca
print(rearrange_string('abbcccc'))
# cbcbcac
print(rearrange_string('abbccccc'))
# None
print(rearrange_string('aaaabbbbccdd'))
# abcabcabdabd
