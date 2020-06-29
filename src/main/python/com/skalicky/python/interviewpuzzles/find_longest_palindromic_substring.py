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


class Solution:
    @staticmethod
    def check_if_palindrome(chars: list, left_pointer: int, right_pointer: int):
        current_left_pointer: int = left_pointer
        current_right_pointer: int = right_pointer
        while current_left_pointer < current_right_pointer:
            if chars[current_left_pointer] != chars[current_right_pointer]:
                return False
            else:
                current_left_pointer = current_left_pointer + 1
                current_right_pointer = current_right_pointer - 1
        return True

    @staticmethod
    def longest_palindrome(s: str):
        if s is None or len(s) == 0:
            return None
        chars: list = list(s)
        substrings_to_check: list = [(0, len(chars) - 1)]
        while len(substrings_to_check) > 0:
            left_pointer, right_pointer = substrings_to_check.pop(0)
            if Solution.check_if_palindrome(chars, left_pointer, right_pointer):
                return s[left_pointer:right_pointer + 1]
            else:
                substrings_to_check.append((left_pointer, right_pointer - 1))
                substrings_to_check.append((left_pointer + 1, right_pointer))
        return None


# Test program
print(str(Solution.longest_palindrome('tracecars')))
# racecar
print(str(Solution.longest_palindrome('banana')))
# anana
print(str(Solution.longest_palindrome('million')))
# illi
print(str(Solution.longest_palindrome('mh')))
# 'm'
print(str(Solution.longest_palindrome('')))
# <None>
print(str(Solution.longest_palindrome(None)))
# <None>
