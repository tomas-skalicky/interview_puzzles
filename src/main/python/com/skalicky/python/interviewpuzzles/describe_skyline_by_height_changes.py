# Task:
#
# Given a list of building in the form of (left, right, height), return what the skyline should look like. The skyline
# should be in the form of a list of (x-axis, height), where x-axis is the next point where there is a change in height
# starting from 0, and height is the new height starting from the x-axis.
#
# Here's some starter code:
#
# def generate_skyline(buildings):
#   # Fill this in.
#
# #            2 2 2
# #            2 2 2
# #        1 1 2 2 2 1 1
# #        1 1 2 2 2 1 1
# #        1 1 2 2 2 1 1
# # pos: 1 2 3 4 5 6 7 8 9
# print generate_skyline([(2, 8, 3), (4, 6, 5)])
# # [(2, 3), (4, 5), (7, 3), (9, 0)]
from enum import Enum
from typing import List, Tuple, Dict


class HeightChange(Enum):
    START = 1,
    END = 2


def generate_skyline(buildings: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    height_changes_by_x: Dict[int, Tuple[int, HeightChange]] = {}
    for building in buildings:
        height_changes_by_x[building[0]] = (building[2], HeightChange.START)
        height_changes_by_x[building[1]] = (building[2], HeightChange.END)

    sorted_xs: List[int] = sorted(height_changes_by_x.keys())
    previous_x: int = 0
    previous_height: int = 0
    resulted_skyline: List[Tuple[int, int]] = []
    for x in sorted_xs:
        height, height_change = height_changes_by_x[x]
        if height_change == HeightChange.START:
            resulted_skyline.append((x, height))
        elif previous_height != height:
            resulted_skyline.append((previous_x + 1, height))
        previous_x = x
        previous_height = height
    resulted_skyline.append((previous_x + 1, 0))
    return resulted_skyline


#            2 2 2
#            2 2 2
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9
print(generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]
