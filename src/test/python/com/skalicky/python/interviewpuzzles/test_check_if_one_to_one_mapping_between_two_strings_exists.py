from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.check_if_one_to_one_mapping_between_two_strings_exists import \
    check_if_one_to_one_mapping_between_two_strings_exists


class Test(TestCase):
    def test_check_if_one_to_one_mapping_between_two_strings_exists__when_input_strings_have_different_length__then_exception_is_raised(
            self):
        self.assertRaisesRegex(RuntimeError, 'Input strings \\[a, ab] do have have the same length.',
                               check_if_one_to_one_mapping_between_two_strings_exists, 'a', 'ab')

    def test_check_if_one_to_one_mapping_between_two_strings_exists__when_mapping_between_characters_exists__then_true_is_returned(
            self):
        self.assertTrue(check_if_one_to_one_mapping_between_two_strings_exists('abc', 'def'))

    def test_check_if_one_to_one_mapping_between_two_strings_exists__when_mapping_between_characters_does_not_exist__then_false_is_returned(
            self):
        self.assertFalse(check_if_one_to_one_mapping_between_two_strings_exists('aac', 'def'))
