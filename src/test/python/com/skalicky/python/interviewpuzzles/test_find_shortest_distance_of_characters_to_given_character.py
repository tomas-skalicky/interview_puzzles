from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_shortest_distance_of_characters_to_given_character import \
    find_shortest_distance_of_characters_to_given_character


class Test(TestCase):
    def test_find_shortest_distance_of_characters_to_given_character__when_input_string_contains_only_1_character__then_output_is_list_with_0(
            self):
        self.assertListEqual([0], find_shortest_distance_of_characters_to_given_character('l', 'l'))

    def test_find_shortest_distance_of_characters_to_given_character__when_input_string_contains_more_same_characters__then_output_is_list_with_0s(
            self):
        self.assertListEqual([0, 0, 0, 0], find_shortest_distance_of_characters_to_given_character('llll', 'l'))

    def test_find_shortest_distance_of_characters_to_given_character__when_input_string_contains_2_different_characters__then_output_is_list_with_0_and_1(
            self):
        self.assertListEqual([0, 1], find_shortest_distance_of_characters_to_given_character('la', 'l'))

    def test_find_shortest_distance_of_characters_to_given_character__when_input_string_contains_given_character_multiple_times_not_next_to_each_other__then_output_list_contains_minimum_distances_out_of_distances_to_all_of_them(
            self):
        self.assertListEqual([2, 1, 0, 0, 1, 2, 2, 1, 0, 1],
                             find_shortest_distance_of_characters_to_given_character('helloworld', 'l'))
