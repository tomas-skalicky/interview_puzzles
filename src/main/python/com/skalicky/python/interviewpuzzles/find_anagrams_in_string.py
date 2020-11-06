# Task:
#
# Given 2 strings s and t, find and return all indexes in string s where t is an anagram.
#
# Here's an example and some starter code:
#
# def find_anagrams(s, t):
#   # Fill this in.
#
# print(find_anagrams('acdbacdacb', 'abc'))
# # [3, 7]
from typing import List, Dict


# Time complexity of the function is O(n) where n is the length of the given text.
def find_anagrams_in_string(text: str, substring: str) -> List[int]:
    text_length: int = len(text)
    substring_length: int = len(substring)
    if text_length < substring_length:
        return []
    else:
        anagram_set: Dict[str, int] = {}
        for character in substring:
            if anagram_set.__contains__(character):
                anagram_set[character] += 1
            else:
                anagram_set[character] = 1

        beginnings_of_anagrams: List[int] = []
        remaining_chars_from_substring: Dict[str, int] = anagram_set.copy()
        for i in range(0, text_length):
            before_head_index: int = i - substring_length
            if before_head_index >= 0:
                before_head_character: str = text[before_head_index]
                if anagram_set.__contains__(before_head_character):
                    if remaining_chars_from_substring.__contains__(before_head_character):
                        if anagram_set[before_head_character] > remaining_chars_from_substring[before_head_character]:
                            remaining_chars_from_substring[before_head_character] += 1
                    else:
                        if anagram_set[before_head_character] > 0:
                            remaining_chars_from_substring[before_head_character] = 1

            current_character: str = text[i]
            if remaining_chars_from_substring.__contains__(current_character) \
                    and remaining_chars_from_substring[current_character] > 0:
                remaining_chars_from_substring[current_character] -= 1
                if remaining_chars_from_substring[current_character] == 0:
                    remaining_chars_from_substring.pop(current_character)
                    if len(remaining_chars_from_substring) == 0:
                        beginnings_of_anagrams.append(before_head_index + 1)
        return beginnings_of_anagrams
