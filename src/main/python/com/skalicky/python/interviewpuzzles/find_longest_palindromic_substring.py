# Task:
#
# A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find
# the longest palindromic substring in s.
#
# Example:
# Input: "banana"
# Output: "anana"
#
# Input: "million"
# Output: "illi"
#
# class Solution:
#     def longestPalindrome(self, s):
#       # Fill this in.
#
# # Test program
# s = "tracecars"
# print(str(Solution().longestPalindrome(s)))
# # racecar
from collections import deque
from typing import Deque, Optional, Tuple


class Solution:
    @staticmethod
    def check_if_palindrome(input_string: str, lowest_index: int, greatest_index_included: int) -> bool:
        current_left_pointer: int = lowest_index
        current_right_pointer: int = greatest_index_included
        while current_left_pointer < current_right_pointer:
            if input_string[current_left_pointer] != input_string[current_right_pointer]:
                return False
            else:
                current_left_pointer += 1
                current_right_pointer -= 1
        return True

    @staticmethod
    def find_longest_palindromic_substring(input_string: Optional[str]) -> Optional[str]:
        if input_string is None or len(input_string) == 0:
            return None
        else:
            # We need both
            # - to efficiently remove from the beginning of the collection and
            # - to efficiently append to the end of the collection,
            # hence we use Deque having a time complexity of O(1) for both of these operations.
            substrings_to_check: Deque[Tuple[int, int]] = deque()
            substrings_to_check.append((0, len(input_string) - 1))
            while len(substrings_to_check) > 0:
                # Picks the longest remaining string to investigate.
                lowest_index, greatest_index_included = substrings_to_check.popleft()
                if Solution.check_if_palindrome(input_string, lowest_index, greatest_index_included):
                    return input_string[lowest_index:greatest_index_included + 1]
                else:
                    substrings_to_check.append((lowest_index, greatest_index_included - 1))
                    substrings_to_check.append((lowest_index + 1, greatest_index_included))
            return None
