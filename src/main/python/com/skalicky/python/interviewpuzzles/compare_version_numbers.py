# Task:
#
# Version numbers are strings that are used to identify unique states of software products. A version number is
# in the format a.b.c.d. and so on where a, b, etc. are numeric strings separated by dots. These generally represent
# a hierarchy from major to minor changes. Given two version numbers version1 and version2, conclude which is
# the latest version number. Your code should do the following:
# If version1 > version2 return 1.
# If version1 < version2 return -1.
# Otherwise return 0.
#
# Note that the numeric strings such as a, b, c, d, etc. may have leading zeroes, and that the version strings do not
# start or end with dots. Unspecified level revision numbers default to 0.
#
# Example:
# Input:
# version1 = "1.0.33"
# version2 = "1.0.27"
# Output: 1
# #version1 > version2
#
# Input:
# version1 = "0.1"
# version2 = "1.1"
# Output: -1
# #version1 < version2
#
# Input:
# version1 = "1.01"
# version2 = "1.001"
# Output: 0
# #ignore leading zeroes, 01 and 001 represent the same number.
#
# Input:
# version1 = "1.0"
# version2 = "1.0.0"
# Output: 0
# #version1 does not have a 3rd level revision number, which
# defaults to "0"
# Here's a starting point
#
# class Solution:
#   def compareVersion(self, version1, version2):
#     # Fill this in.
#
# version1 = "1.0.1"
# version2 = "1"
# print(Solution().compareVersion(version1, version2))
# # 1
from typing import List

PATH_SEPARATOR: str = '.'


class Solution:
    @staticmethod
    def remove_trailing_zeros(version_path: List[str]) -> List[str]:
        version_path_with_removed_zeros: List[str] = list(version_path)
        for i in reversed(range(0, len(version_path))):
            if int(version_path[i]) == 0:
                version_path_with_removed_zeros.pop(i)
            else:
                return version_path_with_removed_zeros
        return version_path_with_removed_zeros

    @staticmethod
    def compare_version_numbers(version1: str, version2: str) -> int:
        version1_parts: List[str] = Solution.remove_trailing_zeros(version1.split(PATH_SEPARATOR))
        version1_part_count: int = len(version1_parts)
        version2_parts: List[str] = Solution.remove_trailing_zeros(version2.split(PATH_SEPARATOR))
        version2_part_count: int = len(version2_parts)
        min_version_part: int = min(version1_part_count, version2_part_count)
        for min_version_part in range(0, min_version_part):
            current_version1_part: int = int(version1_parts[min_version_part])
            current_version2_part: int = int(version2_parts[min_version_part])
            if current_version1_part < current_version2_part:
                return -1
            elif current_version1_part > current_version2_part:
                return 1
        if version1_part_count < version2_part_count:
            return -1
        elif version1_part_count > version2_part_count:
            return 1
        else:
            return 0
