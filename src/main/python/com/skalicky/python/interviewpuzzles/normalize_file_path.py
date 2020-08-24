# Task:
#
# Given a file path with folder names, '..' (Parent directory), and '.' (Current directory), return the shortest
# possible file path (Eliminate all the '..' and '.').
#
# Example
# Input: '/Users/Joma/Documents/../Desktop/./../'
# Output: '/Users/Joma/'
# def shortest_path(file_path):
#   # Fill this in.
#
# print shortest_path('/Users/Joma/Documents/../Desktop/./../')
# # /Users/Joma/
from typing import List


def shortest_path(file_path: str) -> str:
    file_parts: List[str] = file_path.split('/')
    if len(file_path) == 1:
        return file_path
    else:
        result_parts: List[str] = list()
        for part in file_parts:
            if part == '.':
                if len(result_parts) == 0:
                    result_parts.append(part)
            elif part == '..':
                if len(result_parts) == 0:
                    result_parts.append(part)
                else:
                    result_parts.pop()
            else:
                result_parts.append(part)
        return '/'.join(result_parts)


print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/
print(shortest_path('./'))
# ./
print(shortest_path('../'))
# ../
print(shortest_path('../Desktop/./../'))
# ../
