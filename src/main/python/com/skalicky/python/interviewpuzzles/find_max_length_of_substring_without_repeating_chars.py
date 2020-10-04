# Task:
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend
# Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
#
# class Solution:
#   def lengthOfLongestSubstring(self, s):
#     # Fill this in.
#
# print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# # 10
from typing import Optional, Set


class Solution:
    @staticmethod
    def length_of_longest_substring(s: Optional[str]):
        if s is None:
            return 0
        current_max_length: int = 0
        current_length: int = 0
        current_char_set: Set[str] = set()
        for current_char in list(s):
            if current_char_set.__contains__(current_char):
                if current_length > current_max_length:
                    current_max_length = current_length
                current_char_set.clear()
                current_char_set.add(current_char)
                current_length = 1
            else:
                current_char_set.add(current_char)
                current_length = current_length + 1
        return current_max_length


print(Solution.length_of_longest_substring(None))
# 0
print(Solution.length_of_longest_substring(''))
# 0
print(Solution.length_of_longest_substring('abrkaabcdefghijjxxx'))
# 10
