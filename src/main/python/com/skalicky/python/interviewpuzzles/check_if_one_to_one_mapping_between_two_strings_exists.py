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
# Ouput: False # a can't map to d and e
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


def has_character_map(str1: str, str2: str) -> bool:
    str1_length: int = len(str1)
    if str1_length != len(str2):
        raise RuntimeError('Input strings [{}, {}] do have have the same length.'.format(str1, str2))
    else:
        character_map: Dict[str, str] = dict()
        for i in range(0, str1_length):
            char1: str = str1[i:i + 1]
            char2: str = str2[i:i + 1]
            if character_map.__contains__(char1):
                if character_map[char1] != char2:
                    return False
            else:
                character_map[char1] = char2
        return True


print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False
