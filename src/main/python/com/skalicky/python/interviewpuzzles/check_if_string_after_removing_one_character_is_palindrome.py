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


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def check_if_string_after_removing_one_character_is_palindrome(input_string: str) -> bool:
    input_string_length: int = len(input_string)
    for i in range(0, input_string_length):
        if i == 0:
            if is_palindrome(input_string[1:]):
                return True
        elif i == input_string_length - 1:
            if is_palindrome(input_string[:i]):
                return True
        else:
            if is_palindrome(input_string[:i] + input_string[i + 1:]):
                return True
    return False
