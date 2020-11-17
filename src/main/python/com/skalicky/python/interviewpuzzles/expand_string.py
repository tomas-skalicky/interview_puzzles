# Task:
#
# Given a string with a certain rule: k[string] should be expanded to string k times. So for example, 3[abc] should be
# expanded to abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.
#
# Your starting point:
#
# def decodeString(s):
#   # Fill this in.
#
# print decodeString('2[a2[b]c]')
# # abbcabbc
from collections import deque
from typing import Deque, Tuple


def expand_string(input_string: str) -> str:
    evaluation_deque: Deque[Tuple[int, str]] = deque()
    evaluation_deque.append((0, ''))
    last_times_string: str = ''
    last_times: int = 0
    for c in list(input_string):
        if c == '[':
            evaluation_deque.append((last_times, ''))
            last_times_string = ''
            last_times = 0
        elif c == ']':
            current_times, current_string = evaluation_deque.pop()
            parent_times, parent_string = evaluation_deque.pop()
            for i in range(0, current_times):
                parent_string += current_string
            evaluation_deque.append((parent_times, parent_string))
        elif c.isnumeric():
            last_times_string += c
            last_times = last_times * 10 + int(c)
        else:
            current_times, current_string = evaluation_deque.pop()
            if len(last_times_string) > 0:
                current_string += last_times_string
                last_times_string = ''
                last_times = 0
            current_string += c
            evaluation_deque.append((current_times, current_string))
    return evaluation_deque.pop()[1]
