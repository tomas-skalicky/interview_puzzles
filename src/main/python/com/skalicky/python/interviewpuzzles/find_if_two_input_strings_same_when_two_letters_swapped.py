# Task:
#
# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that
# the result equals B.
#
# Example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:
#
# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
# Input: A = "", B = "aa"
# Output: false
# Here's a starting point:
#
# class Solution:
#   def buddyStrings(self, A, B):
#     # Fill this in.
#
# print Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb')
# # True
# print Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb')
# # False
from collections import Counter
from typing import List, Dict


class Solution:
    def buddy_strings(self, a: str, b: str):
        a_length: int = len(a)
        b_length: int = len(b)
        if a_length < 2 or a_length != b_length:
            return False
        else:
            a_chars: List = list(a)
            b_chars: List = list(b)
            if a == b:
                a_occurrences: Dict[str, int] = Counter(a_chars)
                for occurrence in a_occurrences.values():
                    if occurrence > 1:
                        return True
                return False
            else:
                first_index: int = None
                second_index: int = None
                for i in range(0, a_length):
                    if a_chars[i] != b_chars[i]:
                        if first_index is None:
                            first_index = i
                        elif second_index is None:
                            second_index = i
                        else:
                            return False
                return first_index is not None and second_index is not None


print(Solution().buddy_strings('ab', 'ba'))
# True
print(Solution().buddy_strings('ab', 'ab'))
# False
print(Solution().buddy_strings('aa', 'aa'))
# True
print(Solution().buddy_strings('aaa', 'aaa'))
# True
print(Solution().buddy_strings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddy_strings('aaaaaabbc', 'aaaaaaacb'))
# False
print(Solution().buddy_strings('', 'aa'))
# False
