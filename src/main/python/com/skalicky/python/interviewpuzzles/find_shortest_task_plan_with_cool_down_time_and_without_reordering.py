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


def find_shortest_task_plan_with_cool_down_time_and_without_reordering(tasks: List[int], cool_down_time: int) -> int:
    """Assumption: tasks need to be executed in the given order, otherwise the task 2 could have been executed in
     the time 2.
    """

    last_indices_by_tasks: Dict[int, int] = {}
    last_allocated_time: int = 0
    for task in tasks:
        if task in last_indices_by_tasks:
            last_allocated_time = max(last_allocated_time + 1, last_indices_by_tasks[task] + cool_down_time + 1)
        else:
            last_allocated_time += 1
        last_indices_by_tasks[task] = last_allocated_time
    return last_allocated_time
