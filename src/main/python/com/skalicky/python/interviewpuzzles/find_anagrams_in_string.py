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


def find_anagrams_in_string(text: str, substring: str) -> List[int]:
    """Time complexity of the function is O(n) where *n* is the length of the given text.
    """

    text_length: int = len(text)
    substring_length: int = len(substring)
    if text_length < substring_length:
        return []
    else:
        substring_character_occurrence_counts_by_text_characters: Dict[str, int] = {}
        for character in substring:
            if character in substring_character_occurrence_counts_by_text_characters:
                substring_character_occurrence_counts_by_text_characters[character] += 1
            else:
                substring_character_occurrence_counts_by_text_characters[character] = 1

        beginnings_of_anagrams: List[int] = []
        remaining_chars_from_substring: Dict[str, int] = substring_character_occurrence_counts_by_text_characters.copy()
        for i in range(0, text_length):
            before_head_index: int = i - substring_length
            if before_head_index >= 0:
                before_head_character: str = text[before_head_index]
                if before_head_character in substring_character_occurrence_counts_by_text_characters:
                    if before_head_character in remaining_chars_from_substring:
                        if substring_character_occurrence_counts_by_text_characters[before_head_character] > \
                                remaining_chars_from_substring[before_head_character]:
                            remaining_chars_from_substring[before_head_character] += 1
                    else:
                        if substring_character_occurrence_counts_by_text_characters[before_head_character] > 0:
                            remaining_chars_from_substring[before_head_character] = 1

            current_character: str = text[i]
            if current_character in remaining_chars_from_substring and remaining_chars_from_substring[
                current_character] > 0:
                remaining_chars_from_substring[current_character] -= 1
                if remaining_chars_from_substring[current_character] == 0:
                    remaining_chars_from_substring.pop(current_character)
                    if len(remaining_chars_from_substring) == 0:
                        beginnings_of_anagrams.append(before_head_index + 1)
        return beginnings_of_anagrams
