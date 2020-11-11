# Task:
#
# Given a list of strings, find the list of characters that appear in all strings.
#
# Here's an example and some starter code:
#
# def common_characters(strs):
#   # Fill this in.
#
# print(common_characters(['google', 'facebook', 'youtube']))
# # ['e', 'o']
from typing import List, Set


def find_characters_appearing_in_all_strings(strings: List[str]) -> Set[str]:
    string_count: int = len(strings)
    if string_count == 0:
        return set()
    else:
        common_characters: Set[str] = set(strings[0])
        for i in range(1, string_count):
            new_common_characters: Set[str] = set()
            for character in list(strings[i]):
                if character in common_characters:
                    new_common_characters.add(character)
            common_characters = new_common_characters
        return common_characters
