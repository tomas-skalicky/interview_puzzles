# Task:
#
# You are the manager of a number of employees who all sit in a row. The CEO would like to give bonuses to all of your
# employees, but since the company did not perform so well this year the CEO would like to keep the bonuses to
# a minimum.
#
# The rules of giving bonuses is that:
# - Each employee begins with a bonus factor of 1x.
# - For each employee, if they perform better than the person sitting next to them, the employee is given +1 higher
# bonus (and up to +2 if they perform better than both people to their sides).
#
# Given a list of employee's performance, find the bonuses each employee should get.
#
# Example:
# Input: [1, 2, 3, 2, 3, 5, 1]
# Output: [1, 2, 3, 1, 2, 3, 1]
# Here's your starting point:
#
# def getBonuses(performance):
#   # Fill this in.
#
# print getBonuses([1, 2, 3, 2, 3, 5, 1])
# # [1, 2, 3, 1, 2, 3, 1]
from typing import List


def calculate_employees_bonuses(employees_performance: List[int]) -> List[int]:
    employee_count: int = len(employees_performance)
    bonuses: List[int] = []
    for i in range(0, employee_count):
        current_bonus: int = 1
        current_performance: int = employees_performance[i]
        if i != 0 and employees_performance[i - 1] < current_performance:
            current_bonus += 1
        if i != employee_count - 1 and employees_performance[i + 1] < current_performance:
            current_bonus += 1
        bonuses.append(current_bonus)
    return bonuses
