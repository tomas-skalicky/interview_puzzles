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


class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            valid_tuples = {'}': '{', ')': '(', ']': '['}
            chars = list(s)
            stack = []
            for c in chars:
                if valid_tuples.__contains__(c):
                    expected_opening_char = valid_tuples.get(c)
                    if len(stack) == 0:
                        return False
                    else:
                        actual_opening_char = stack.pop(0)
                        if actual_opening_char != expected_opening_char:
                            return False
                else:
                    stack.insert(0, c)
            if len(stack) == 0:
                return True
            else:
                return False
