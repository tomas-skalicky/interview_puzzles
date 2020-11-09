from typing import Dict, List
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_words_buildable_from_letters import \
    find_words_buildable_from_letters


class Test(TestCase):
    def test_find_words_buildable_from_letters__when_input_is_valid__then_there_is_ouput(self):
        letter_lists_by_digits: Dict[int, List[str]] = {
            1: [],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
            0: []
        }
        valid_words: List[str] = ['dog', 'fish', 'cat', 'fog']
        self.assertListEqual(['dog', 'fog'],
                             find_words_buildable_from_letters('364', letter_lists_by_digits, valid_words))
