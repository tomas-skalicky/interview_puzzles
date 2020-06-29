# Task:
#
# Given a string with the initial condition of dominoes, where:
#
# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side
#
# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force
# cancels out and that domino remains upright.
#
# Example:
# Input:  ..R...L..R.
# Output: ..RR.LL..RR
# Here is your starting point:
#
# class Solution(object):
#   def pushDominoes(self, dominoes):
#     # Fill this in.
#
# print Solution().pushDominoes('..R...L..R.')
# # ..RR.LL..RR
from math import floor
from typing import List


class Solution:
    @staticmethod
    def push_dominoes(dominoes_string):
        dominoes: List[str] = list(dominoes_string)
        right_index: int = None
        domino_length = len(dominoes)
        for i in range(0, domino_length):
            c: str = dominoes[i]
            if c == 'L':
                if right_index:
                    for j in range(right_index + 1, floor(i - right_index / 2)):
                        if j == i + right_index - j:
                            break
                        dominoes[j] = 'R'
                        dominoes[i + right_index - j] = 'L'
                    right_index = None
                else:
                    for j in range(0, i):
                        dominoes[j] = 'L'
            elif c == 'R':
                if right_index:
                    for j in range(right_index + 1, i):
                        dominoes[j] = 'R'
                right_index = i
        if right_index:
            for i in range(right_index + 1, domino_length):
                dominoes[i] = 'R'
        return ''.join(dominoes)


print(Solution.push_dominoes('..R...L..R.'))
# ..RR.LL..RR
print(Solution.push_dominoes('..R.R.L..R.'))
# ..RRR.L..RR
print(Solution.push_dominoes('..R..RL..R.'))
# ..RRRRL..RR
print(Solution.push_dominoes('..L...L..R.'))
# LLLLLLL..RR
print(Solution.push_dominoes('...'))
# ...
print(Solution.push_dominoes(''))
# <empty>
