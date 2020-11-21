from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_longest_common_prefix import find_longest_common_prefix


class Test(TestCase):
    def test_find_longest_common_prefix__when_input_is_empty__then_output_is_empty_string(
            self):
        self.assertEqual('', find_longest_common_prefix([]))

    def test_find_longest_common_prefix__when_input_is_1_string__then_output_is_this_string(
            self):
        self.assertEqual('helloworld', find_longest_common_prefix(['helloworld']))

    def test_find_longest_common_prefix__when_common_prefix_is_non_empty_and_equals_one_input_string__then_output_is_that_input_string(
            self):
        self.assertEqual('hell', find_longest_common_prefix(['helloworld', 'hellokitty', 'hell']))

    def test_find_longest_common_prefix__when_common_prefix_is_non_empty_and_is_not_equal_to_any_input_string__then_output_is_common_prefix(
            self):
        self.assertEqual('hello', find_longest_common_prefix(['helloworld', 'hellokitty', 'helloy']))

    def test_find_longest_common_prefix__when_there_is_no_common_prefix__then_output_is_empty(self):
        self.assertEqual('', find_longest_common_prefix(['daily', 'interview', 'pro']))
