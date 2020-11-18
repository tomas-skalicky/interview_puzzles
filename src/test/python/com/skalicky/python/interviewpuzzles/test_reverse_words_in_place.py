from typing import List
from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.reverse_words_in_place import reverse_words_in_place


class Test(TestCase):
    def test_reverse_words_in_place__when_input_contains_only_1_word__then_input_is_not_changed(self):
        input_characters: List[str] = list('you')
        reverse_words_in_place(input_characters)
        self.assertListEqual(list('you'), input_characters)

    def test_reverse_words_in_place__when_input_contains_2_words__then_words_are_swapped(self):
        input_characters: List[str] = list('you two')
        reverse_words_in_place(input_characters)
        self.assertListEqual(list('two you'), input_characters)

    def test_reverse_words_in_place__when_input_contains_2_words_with_different_lengths__then_word_are_swapped(self):
        input_characters: List[str] = list('you this')
        reverse_words_in_place(input_characters)
        self.assertListEqual(list('this you'), input_characters)

    def test_reverse_words_in_place__when_input_contains_3_words__then_word_in_middle_stay_in_middle(self):
        input_characters: List[str] = list('you read this')
        reverse_words_in_place(input_characters)
        self.assertListEqual(list('this read you'), input_characters)

    def test_reverse_words_in_place__when_input_contains_4_words___then_words_are_swapped(self):
        input_characters: List[str] = list('can read you this')
        reverse_words_in_place(input_characters)
        self.assertListEqual(list('this you read can'), input_characters)
