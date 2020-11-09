from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_witnesses_of_murder import find_witnesses_of_murder


class Test(TestCase):
    def test_find_witnesses_of_murder__when_there_is_nobody__then_there_is_no_witness(self):
        self.assertEqual(0, find_witnesses_of_murder([]))

    def test_find_witnesses_of_murder__when_there_is_only_1_person__then_there_is_1_witness(self):
        self.assertEqual(1, find_witnesses_of_murder([3]))

    def test_find_witnesses_of_murder__when_there_are_people_smaller_than_successors__then_they_are_not_witnesses(self):
        self.assertEqual(3, find_witnesses_of_murder([3, 6, 3, 4, 1]))
