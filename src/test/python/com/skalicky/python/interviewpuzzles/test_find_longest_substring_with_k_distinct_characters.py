from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_longest_substring_with_k_distinct_characters import \
    find_longest_substring_with_k_distinct_characters


class Test(TestCase):
    def test_find_longest_substring_with_k_distinct_characters__when_input_is_aabcdefff_and_3__then_output_is_defff(
            self):
        self.assertTupleEqual((5, 'defff'), find_longest_substring_with_k_distinct_characters('aabcdefff', 3))

    def test_find_longest_substring_with_k_distinct_characters__when_input_is_aabacadefff_and_3__then_output_is_aabaca(
            self):
        self.assertTupleEqual((6, 'aabaca'), find_longest_substring_with_k_distinct_characters('aabacadefff', 3))

    def test_find_longest_substring_with_k_distinct_characters__when_input_string_has_less_distinct_characters_than_k__then_output_is_whole_input_string(
            self):
        self.assertTupleEqual((6, 'aabaca'), find_longest_substring_with_k_distinct_characters('aabaca', 4))
