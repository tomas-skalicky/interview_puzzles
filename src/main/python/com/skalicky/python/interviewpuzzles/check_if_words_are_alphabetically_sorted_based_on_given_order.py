# Task:
#
# Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical
# order.
#
# Example:
# Input:
# words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"
#
# Output: False
# Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'
#
# Example 2:
# Input:
# words = ["zyx", "zyxw", "zyxwy"],
# order="zyxwvutsrqponmlkjihgfedcba"
#
# Output: True
# Explanation: The words are in increasing alphabetical order
#
# Here's a starting point:
#
# def isSorted(words, order):
#   # Fill this in.
#
# print isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba")
# # False
# print isSorted(["zyx", "zyxw", "zyxwy"],
#                "zyxwvutsrqponmlkjihgfedcba")
# # True
from typing import List, Dict


def get_character_order(index: int, word: str, orders_by_chars: Dict[str, int]) -> int:
    if index >= len(word):
        return -1
    else:
        return orders_by_chars[word[index]]


def is_sorted(words: List[str], order: str) -> bool:
    if len(words) == 1:
        return True
    else:
        order_chars: List[str] = list(order)
        orders_by_chars: Dict[str, int] = dict()
        for i in range(0, len(order)):
            orders_by_chars[order_chars[i]] = i
        word_max_length: int = 0
        for word in words:
            word_max_length = max(word_max_length, len(word))
        word_count: int = len(words)
        for i in range(0, word_max_length):
            previous_order: int = get_character_order(i, words[0], orders_by_chars)
            for j in range(1, word_count):
                current_order: int = get_character_order(i, words[j], orders_by_chars)
                if previous_order > current_order:
                    return False
                previous_order = current_order
        return True


print(is_sorted(["abcd"], "zyxwvutsrqponmlkjihgfedcba"))
# True
print(is_sorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(is_sorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))
# True
print(is_sorted(["zyxz", "zyx"], "zyxwvutsrqponmlkjihgfedcba"))
# False
