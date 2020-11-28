from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.combine_integers_to_largest_possible_number import \
    combine_integers_to_largest_possible_number


class Test(TestCase):
    def test_combine_integers_to_largest_possible_number__when_list_consists_of_17_7_2_45_72__then_result_is_77245217(
            self):
        self.assertEqual('77245217', combine_integers_to_largest_possible_number([17, 7, 2, 45, 72]))

    def test_combine_integers_to_largest_possible_number__when_list_consists_of_72_7__then_result_is_772(
            self):
        self.assertEqual('772', combine_integers_to_largest_possible_number([72, 7]))

    def test_combine_integers_to_largest_possible_number__when_list_consists_of_7_78__then_result_is_787(
            self):
        self.assertEqual('787', combine_integers_to_largest_possible_number([7, 78]))
