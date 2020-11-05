# Task:
#
# We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time, but we
# cannot run the same task simultaneously.
#
# Given a list of tasks, find how long it will take to complete the tasks in the order they are input.
# tasks = [1, 1, 2, 1]
# cooldown = 2
# output: 7 (order is 1 _ _ 1 2 _ 1)
# def findTime(arr, cooldown):
#   # Fill this in.
#
# print findTime([1, 1, 2, 1], 2)
# # 7
from typing import List, Dict


# Assumption: tasks need to be executed in the given order, otherwise the task 2 could have been executed in the time 2.
def find_time(arr: List[int], cooldown: int) -> int:
    last_indices_by_tasks: Dict[int, int] = {}
    last_allocated_time: int = 0
    for task in arr:
        if last_indices_by_tasks.__contains__(task):
            last_allocated_time = max(last_allocated_time + 1, last_indices_by_tasks[task] + cooldown + 1)
        else:
            last_allocated_time += 1
        last_indices_by_tasks[task] = last_allocated_time
    return last_allocated_time


print(find_time([1, 1, 2, 1], 2))
# 7
print(find_time([1, 2, 3, 1], 1))
# 4
