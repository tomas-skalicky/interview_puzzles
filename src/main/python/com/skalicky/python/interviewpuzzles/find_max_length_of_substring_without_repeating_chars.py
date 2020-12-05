# Task:
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend
# Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
#
# class Solution:
#     @staticmethod
#     def find_max_length_of_substring_without_repeating_chars(s):
#         # Fill this in.
#
# print(Solution.find_max_length_of_substring_without_repeating_chars('abrkaabcdefghijjxxx'))
# # 10
from typing import Optional, Set


class Solution:
    @staticmethod
    def find_max_length_of_substring_without_repeating_chars(s: Optional[str]):
        if s is None:
            return 0
        else:
            current_max_length: int = 0
            current_length: int = 0
            current_char_set: Set[str] = set()
            for current_char in s:
                if current_char in current_char_set:
                    if current_length > current_max_length:
                        current_max_length = current_length
                    current_char_set.clear()
                    current_char_set.add(current_char)
                    current_length = 1
                else:
                    current_char_set.add(current_char)
                    current_length += 1
            return max(current_length, current_max_length)
