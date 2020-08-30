# Task:
#
# An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.
#
# Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts
# of A, B, C, D.
#
# Keep in mind that integers can't start with a 0! (Except for 0)
#
# Example:
# Input: 1592551013
# Output: ['159.255.101.3', '159.255.10.13']
# def ip_addresses(s, ip_parts=[]):
#   # Fill this in.
#
# print ip_addresses('1592551013')
# # ['159.255.101.3', '159.255.10.13']
from typing import List


def is_valid_ip_address_part(ip_address_part: str) -> bool:
    return (len(ip_address_part) == 1 or ip_address_part[0] != '0') and int(ip_address_part) <= 255


def ip_addresses(s: str) -> List[str]:
    s_length: int = len(s)
    collected_addresses: List[str] = []
    for part1_end_index_included in range(0, min(3, s_length - 3)):
        part1: str = s[0:part1_end_index_included + 1]
        if is_valid_ip_address_part(part1):
            part2_start_index: int = part1_end_index_included + 1
            for part2_end_index_included in range(part2_start_index, min(part2_start_index + 3, s_length - 2)):
                part2: str = s[part2_start_index:part2_end_index_included + 1]
                if is_valid_ip_address_part(part2):
                    part3_start_index: int = part2_end_index_included + 1
                    for part3_end_index_included in range(part3_start_index, min(part3_start_index + 3, s_length - 1)):
                        part3: str = s[part3_start_index:part3_end_index_included + 1]
                        part4: str = s[part3_end_index_included + 1:]
                        if is_valid_ip_address_part(part3) and is_valid_ip_address_part(part4):
                            collected_addresses.append('.'.join([part1, part2, part3, part4]))
    return collected_addresses


print(ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']
print(ip_addresses('1592551000'))
# ['159.255.100.0']
print(ip_addresses('8888'))
# ['8.8.8.8']
