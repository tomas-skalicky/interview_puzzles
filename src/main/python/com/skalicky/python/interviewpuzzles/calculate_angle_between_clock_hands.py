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


def calculate_angle_between_clock_hands(hours: int, minutes: int) -> int:
    minutes_per_clock: int = 60
    hours_per_clock: int = 12
    angle_between_60_and_minute_hand: int = minutes * floor(360 / minutes_per_clock)
    angle_between_12_and_hour_hand: int = hours % hours_per_clock * floor(360 / hours_per_clock)
    angle_between_hours_and_hour_hand: int = floor(angle_between_60_and_minute_hand / hours_per_clock)
    return abs(angle_between_12_and_hour_hand + angle_between_hours_and_hour_hand - angle_between_60_and_minute_hand)
