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


def calc_angle(h: int, m: int) -> int:
    minutes_per_clock: int = 60
    hours_per_clock: int = 12
    angle_between_60_and_m: int = m * floor(360 / minutes_per_clock)
    angle_between_12_and_h: int = h % hours_per_clock * floor(360 / hours_per_clock)
    angle_between_h_and_hour_hand: int = floor(angle_between_60_and_m / hours_per_clock)
    return abs(angle_between_12_and_h + angle_between_h_and_hour_hand - angle_between_60_and_m)


print(calc_angle(3, 30))
# 75
print(calc_angle(15, 30))
# 75
print(calc_angle(12, 30))
# 165
print(calc_angle(1, 0))
# 30
print(calc_angle(12, 0))
# 0
