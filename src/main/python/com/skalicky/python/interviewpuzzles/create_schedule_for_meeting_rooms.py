# Task:
#
# Given a list of meetings that will happen during a day, find the minimum number of meeting rooms that can fit all
# meetings.
#
# Each meeting will be represented by a tuple of (start_time, end_time), where both start_time and end_time will be
# represented by an integer to indicate the time. start_time will be inclusive, and end_time will be exclusive, meaning
# a meeting of (0, 10) and (10, 20) will only require 1 meeting room.
#
# Here's some examples and some starting code:
#
# def meeting_rooms(meetings):
#   # Fill this in.
#
# # print 1
# print(meeting_rooms([(0, 10), (10, 20)]))
# # 1
#
# print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# # 3 (all meetings overlap at time 20)
from bisect import bisect, insort_left
from collections import deque
from functools import total_ordering
from typing import Tuple, List, Dict, Deque


@total_ordering
class RoomAllocation:
    def __init__(self, start_of_first_meeting: int, end_of_first_meeting: int):
        self.start_of_first_meeting: int = start_of_first_meeting
        self.end_of_last_meeting: int = end_of_first_meeting

    def __eq__(self, other):
        return self.start_of_first_meeting == other.start_of_first_meeting \
               and self.end_of_last_meeting == other.end_of_last_meeting

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other) -> bool:
        return self.start_of_first_meeting < other.start_of_first_meeting or (
                self.start_of_first_meeting == other.start_of_first_meeting and self.end_of_last_meeting < other.end_of_last_meeting)


# Time complexity ... O(n log n) where n is the number of meetings because n >= r where r is the number of necessary
# meeting rooms
def meeting_rooms(meetings: List[Tuple[int, int]]) -> int:
    # Time complexity ... O(n log n) where n is the number of meetings
    sorted_meetings: List[Tuple[int, int]] = sorted(meetings)
    next_meeting_room_number: int = 1
    sorted_rooms_by_end_of_last_meeting_asc: Deque[RoomAllocation] = deque()
    # Time complexity ... O(n log r) where n is the number of meetings and r is the number of necessary meeting rooms
    for meeting in sorted_meetings:
        if meeting[0] != meeting[1]:
            if len(sorted_rooms_by_end_of_last_meeting_asc) == 0:
                new_room: RoomAllocation = RoomAllocation(meeting[0], meeting[1])
                sorted_rooms_by_end_of_last_meeting_asc.append(new_room)
                next_meeting_room_number += 1
            else:
                room_with_least_end: RoomAllocation = sorted_rooms_by_end_of_last_meeting_asc.popleft()
                if room_with_least_end.end_of_last_meeting <= meeting[0]:
                    room_with_least_end.end_of_last_meeting = meeting[1]
                    insort_left(sorted_rooms_by_end_of_last_meeting_asc, room_with_least_end)
                else:
                    sorted_rooms_by_end_of_last_meeting_asc.appendleft(room_with_least_end)
                    new_room: RoomAllocation = RoomAllocation(meeting[0], meeting[1])
                    insort_left(sorted_rooms_by_end_of_last_meeting_asc, new_room)
                    next_meeting_room_number += 1
    return next_meeting_room_number - 1
