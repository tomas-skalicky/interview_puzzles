# Task:
#
# Given a string, return the first recurring letter that appears. If there are no recurring letters, return None.
#
# Example:
#
# Input: qwertty
# Output: t
#
# Input: qwerty
# Output: None
#
# Here's some starter code:
#
# def first_recurring_char(s):
#   # Fill this in.
#
# print(first_recurring_char('qwertty'))
# # t
#
# print(first_recurring_char('qwerty'))
# # None


def first_recurring_char(s: str) -> str:
    if s is None:
        return None
    else:
        string_length: int = len(s)
        if string_length < 2:
            return None
        else:
            previous_character: str = s[0]
            for i in range(1, string_length):
                current_character: str = s[i]
                if current_character == previous_character:
                    return previous_character
                else:
                    previous_character = current_character
            return None


print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None

print(first_recurring_char('qwertyt'))
# None

print(first_recurring_char('qwerttyy'))
# t

print(first_recurring_char('q'))
# None

print(first_recurring_char(''))
# None

print(first_recurring_char(None))
# None
