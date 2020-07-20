# Task:
#
# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.
#
# def calcAngle(h, m):
#   # Fill this in.
#
# print calcAngle(3, 30)
# # 75
# print calcAngle(12, 30)
# # 165
from math import floor


def calc_angle(h: int, m: int):
    hour_angle_from_12: int = h % 12 * floor(360 / 12)
    minute_angle_from_12: int = m % 60 * floor(360 / 60)
    return abs(hour_angle_from_12 - minute_angle_from_12)


print(calc_angle(3, 30))
# 90
print(calc_angle(12, 30))
# 180
print(calc_angle(1, 0))
# 30
print(calc_angle(12, 0))
# 0
