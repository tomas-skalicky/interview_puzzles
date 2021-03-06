# Task:
#
# Given a phone number, return all valid words that can be created using that phone number.
#
# For instance, given the phone number 364
# we can construct the words ['dog', 'fog'].
#
# Here's a starting point:
#
# lettersMaps = {
#     1: [],
#     2: ['a', 'b', 'c'],
#     3: ['d', 'e', 'f'],
#     4: ['g', 'h', 'i'],
#     5: ['j', 'k', 'l'],
#     6: ['m', 'n', 'o'],
#     7: ['p', 'q', 'r', 's'],
#     8: ['t', 'u', 'v'],
#     9: ['w', 'x', 'y', 'z'],
#     0: []
# }
#
# validWords = ['dog', 'fish', 'cat', 'fog']
#
# def makeWords(phone):
#   #Fill this in
#
# print(makeWords('364'))
# # ['dog', 'fog']
from typing import Dict, List


def count_letters(word: str) -> Dict[str, int]:
    occurrences_by_letters: Dict[str, int] = {}
    for letter in list(word):
        if letter in occurrences_by_letters:
            occurrences_by_letters[letter] += 1
        else:
            occurrences_by_letters[letter] = 1
    return occurrences_by_letters


def find_words_buildable_from_letters(phone_number: str, letter_lists_by_digits, valid_words) -> List[str]:
    occurrences_by_digit_strings: Dict[str, int] = count_letters(phone_number)
    occurrences_by_letters_in_phone_number: Dict[str, int] = {}
    for digit_string in occurrences_by_digit_strings.keys():
        digit_occurrence: int = occurrences_by_digit_strings[digit_string]
        for letter in letter_lists_by_digits[int(digit_string)]:
            if letter in occurrences_by_letters_in_phone_number:
                occurrences_by_letters_in_phone_number[letter] += digit_occurrence
            else:
                occurrences_by_letters_in_phone_number[letter] = digit_occurrence

    buildable_words: List[str] = []
    for valid_word in valid_words:
        occurrences_by_letters_in_valid_word: Dict[str, int] = count_letters(valid_word)
        can_by_built: bool = True
        for letter_in_valid_word in occurrences_by_letters_in_valid_word.keys():
            letter_occurrence: int = occurrences_by_letters_in_valid_word[letter_in_valid_word]
            if letter_in_valid_word not in occurrences_by_letters_in_phone_number or \
                    occurrences_by_letters_in_phone_number[letter_in_valid_word] < letter_occurrence:
                can_by_built = False
                break
        if can_by_built:
            buildable_words.append(valid_word)

    return buildable_words
