# Task:
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.
#
# Example:
# Input: "((()))"
# Output: True
#
# Input: "[()]{}"
# Output: True
#
# Input: "({[)]"
# Output: False
#
# class Solution:
#   def isValid(self, s):
#     # Fill this in.
#
# # Test Program
# s = "()(){(())"
# # should return False
# print(Solution().isValid(s))
#
# s = ""
# # should return True
# print(Solution().isValid(s))
#
# s = "([{}])()"
# # should return True
# print(Solution().isValid(s))
from collections import deque
from typing import Deque


class Solution:
    @staticmethod
    def validate_closing_of_parentheses(input_string: str) -> bool:
        if len(input_string) == 0:
            return True
        else:
            valid_tuples = {'}': '{', ')': '(', ']': '['}
            characters = list(input_string)
            stack: Deque[str] = deque()
            for current_character in characters:
                if valid_tuples.__contains__(current_character):
                    expected_opening_character = valid_tuples.get(current_character)
                    if len(stack) == 0:
                        return False
                    else:
                        actual_opening_character: str = stack.popleft()
                        if actual_opening_character != expected_opening_character:
                            return False
                else:
                    stack.appendleft(current_character)
            return len(stack) == 0
