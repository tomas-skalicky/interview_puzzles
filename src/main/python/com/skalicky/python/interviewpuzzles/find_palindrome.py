# Task:
#
# Given a string, determine if there is a way to arrange the string such that the string is a palindrome. If such
# arrangement exists, return a palindrome (There could be many arrangements). Otherwise return None.
#
# Here's some starter code:
#
# def find_palindrome(s):
#   # Fill this in.
#
# print(find_palindrome('momom'))
# # momom
from collections import deque
from math import floor
from typing import Deque, Dict, List, Optional


def find_palindrome(s: str) -> Optional[str]:
    characters: List[str] = list(s)
    occurrence_count_by_characters: Dict[str, int] = {}
    for current_char in characters:
        occurrence_count_by_characters[current_char] = occurrence_count_by_characters[
                                                           current_char] + 1 if current_char in occurrence_count_by_characters else 1

    char_with_odd_occurrences: Optional[str] = None

    for current_char in occurrence_count_by_characters.keys():
        if occurrence_count_by_characters[current_char] % 2 == 1:
            if char_with_odd_occurrences is None:
                char_with_odd_occurrences = current_char
            else:
                return None

    result_string_deque: Deque[str] = deque(char_with_odd_occurrences)
    for current_char in occurrence_count_by_characters.keys():
        for i in range(0, floor(occurrence_count_by_characters[current_char] / 2)):
            result_string_deque.appendleft(current_char)
            result_string_deque.append(current_char)
    return ''.join(result_string_deque)


print(find_palindrome('momom'))
# ommmo
print(find_palindrome('mommo'))
# ommmo
print(find_palindrome('mmrrmommo'))
# ormmmmmro
print(find_palindrome('moommo'))
# None
