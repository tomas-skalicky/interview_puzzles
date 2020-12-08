from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_all_concatenated_words_in_dictionary import Solution


class TestSolution(TestCase):
    def test_find_all_concatenated_words_in_dictionary__when_input_contains_words_of_same_length__then_output_is_empty(
            self):
        self.assertSetEqual(set(), Solution.find_all_concatenated_words_in_dictionary({'cat', 'dog', 'eat'}))

    def test_find_all_concatenated_words_in_dictionary__when_input_contains_multiple_concatenated_words_of_2_other_words__then_these_words_are_in_output(
            self):
        self.assertSetEqual({'techlead', 'catsdog'}, Solution.find_all_concatenated_words_in_dictionary(
            {'tech', 'lead', 'techlead', 'cat', 'cats', 'dog', 'catsdog'}))

    def test_find_all_concatenated_words_in_dictionary__when_input_contains_concatenated_word_of_3_other_words__then_this_word_is_in_output(
            self):
        self.assertSetEqual({'catsdog'}, Solution.find_all_concatenated_words_in_dictionary(
            {'cat', 's', 'dog', 'catsdog'}))

    def test_find_all_concatenated_words_in_dictionary__when_input_contains_word_concatenated_by_multiple_ways__then_this_word_is_in_output(
            self):
        self.assertSetEqual({'cats', 'catsdog'}, Solution.find_all_concatenated_words_in_dictionary(
            {'cat', 'cats', 's', 'dog', 'catsdog'}))
