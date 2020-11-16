# Task:
#
# Given two strings, find if there is a one-to-one mapping of characters between the two strings.
#
# Example
#
# Input: abc, def
# Output: True # a -> d, b -> e, c -> f
#
# Input: aab, def
# Output: False # a can't map to d and e
#
# Here's some starter code:
#
# def has_character_map(str1, str2):
#   # Fill this in.
#
# print(has_character_map('abc', 'def'))
# # True
# print(has_character_map('aac', 'def'))
# # False
from typing import Dict


def check_if_one_to_one_mapping_between_two_strings_exists(string1: str, string2: str) -> bool:
    string1_length: int = len(string1)
    if string1_length != len(string2):
        raise RuntimeError('Input strings [{}, {}] do have have the same length.'.format(string1, string2))
    else:
        character_map: Dict[str, str] = {}
        for i in range(0, string1_length):
            character_in_string1: str = string1[i:i + 1]
            character_in_string2: str = string2[i:i + 1]
            if character_map.__contains__(character_in_string1):
                if character_map[character_in_string1] != character_in_string2:
                    return False
            else:
                character_map[character_in_string1] = character_in_string2
        return True
