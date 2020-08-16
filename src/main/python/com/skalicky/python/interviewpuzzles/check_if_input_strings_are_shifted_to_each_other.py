# Task:
#
# You are given two strings, A and B. Return whether A can be shifted some number of times to get B.
#
# Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb
# should return false.
#
# def is_shifted(a, b):
#   # Fill this in.
#
# print is_shifted('abcde', 'cdeab')
# # True
from typing import List


def is_shifted(a: str, b: str) -> bool:
    a_length: int = len(a)
    if a_length != len(b):
        return False
    else:
        a_list: List[str] = list(a)
        b_list: List[str] = list(b)
        for start_index_in_a in range(0, a_length):
            shifted_strings: bool = True
            for i in range(start_index_in_a, start_index_in_a + a_length):
                index_in_a: int = i % a_length
                if a_list[index_in_a] != b_list[i - start_index_in_a]:
                    shifted_strings = False
            if shifted_strings:
                return True
        return False


print(is_shifted('abcde', 'cdeab'))
# True
print(is_shifted('abc', 'acb'))
# False
print(is_shifted('abc', 'abc '))
# False
