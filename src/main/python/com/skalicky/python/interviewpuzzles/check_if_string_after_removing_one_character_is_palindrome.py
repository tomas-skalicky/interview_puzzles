# Task:
#
# Given a string, determine if you can remove any character to create a palindrome.
#
# Here's some examples and some starter code:
#
# def create_palindrome(s):
#   # Fill this in.
#
# print(create_palindrome("abcdcbea"))
# # True
# print(create_palindrome("abccba"))
# # True
# print(create_palindrome("abccaa"))
# # False


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def create_palindrome(s: str) -> bool:
    s_length: int = len(s)
    for i in range(0, s_length):
        if i == 0:
            if is_palindrome(s[1:]):
                return True
        elif i == s_length - 1:
            if is_palindrome(s[:i]):
                return True
        else:
            if is_palindrome(s[:i] + s[i + 1:]):
                return True
    return False
