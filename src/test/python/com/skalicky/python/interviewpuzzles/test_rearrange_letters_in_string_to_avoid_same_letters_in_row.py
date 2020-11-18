from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.rearrange_letters_in_string_to_avoid_same_letters_in_row import \
    rearrange_letters_in_string_to_avoid_same_letters_in_row


class Test(TestCase):
    def test_rearrange_letters_in_string_to_avoid_same_letters_in_row__when_input_contains_only_1_letter__then_result_is_same_as_input(
            self):
        self.assertEqual('a', rearrange_letters_in_string_to_avoid_same_letters_in_row('a'))

    def test_rearrange_letters_in_string_to_avoid_same_letters_in_row__when_input_contains_even_number_of_letters_and_half_of_its_length_is_occupied_by_one_letter__then_solution_is_found_and_result_starts_but_not_ends_with_that_letter(
            self):
        self.assertEqual('cbcbca', rearrange_letters_in_string_to_avoid_same_letters_in_row('abbccc'))

    def test_rearrange_letters_in_string_to_avoid_same_letters_in_row__when_input_contains_odd_number_of_letters_and_half_of_its_length_plus_1_is_occupied_by_one_letter__then_solution_is_found_and_result_starts_and_ends_with_that_letter(
            self):
        self.assertEqual('cbcbcac', rearrange_letters_in_string_to_avoid_same_letters_in_row('abbcccc'))

    def test_rearrange_letters_in_string_to_avoid_same_letters_in_row__when_input_contains_even_number_of_letters_and_more_than_half_of_its_length_is_occupied_by_one_letter__then_no_solution_exists_hence_result_is_none(
            self):
        self.assertIsNone(rearrange_letters_in_string_to_avoid_same_letters_in_row('abbccccc'))

    def test_rearrange_letters_in_string_to_avoid_same_letters_in_row__when_input_is_aaaabbbbccdd__then_result_is_abcabcabdabd(
            self):
        self.assertEqual('abcabcabdabd', rearrange_letters_in_string_to_avoid_same_letters_in_row('aaaabbbbccdd'))
