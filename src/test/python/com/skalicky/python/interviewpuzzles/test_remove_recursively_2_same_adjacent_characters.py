from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.remove_recursively_2_same_adjacent_characters import \
    remove_recursively_2_same_adjacent_characters


class Test(TestCase):
    def test_remove_recursively_2_same_adjacent_characters__when_input_is_cabba__then_there_are_two_removals_and_output_is_c(
            self):
        self.assertEqual('c', remove_recursively_2_same_adjacent_characters('cabba'))

    def test_remove_recursively_2_same_adjacent_characters__when_input_consists_of_3_same_acjacent_characters__then_1_character_out_of_them_is_left(
            self):
        self.assertEqual('a', remove_recursively_2_same_adjacent_characters('aaa'))

    def test_remove_recursively_2_same_adjacent_characters__when_input_consists_of_4_same_acjacent_characters__then_output_is_empty(
            self):
        self.assertEqual('', remove_recursively_2_same_adjacent_characters('aaaa'))
