from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.create_schedule_for_meeting_rooms import meeting_rooms


class Test(TestCase):
    def test_meeting_rooms__when_one_meeting_starts_after_another__then_one_room_is_necessary(self):
        self.assertEqual(1, meeting_rooms([(0, 10), (10, 20)]))

    def test_meeting_rooms__when_meetings_overlap_each_other__then_more_rooms_are_necessary(self):
        self.assertEqual(3, meeting_rooms([(20, 30), (10, 21), (0, 50)]))

    def test_meeting_rooms__when_there_is_no_meeting__then_no_room_is_necessary(self):
        self.assertEqual(0, meeting_rooms([]))

    def test_meeting_rooms__when_meeting_takes_no_time__then_no_room_is_necessary(self):
        self.assertEqual(0, meeting_rooms([(10, 10)]))
