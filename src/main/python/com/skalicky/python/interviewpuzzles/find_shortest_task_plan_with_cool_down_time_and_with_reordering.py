# Task:
#
# A task is a some work to be done which can be assumed takes 1 unit of time. Between the same type of tasks you must
# take at least n units of time before running the same tasks again.
#
# Given a list of tasks (each task will be represented by a string), and a positive integer n representing the time it
# takes to run the same task again, find the minimum amount of time needed to run all tasks.
#
# Here's an example and some starter code:
#
# def schedule_tasks(tasks, n):
#   # Fill this in.
#
# print(schedule_tasks(['q', 's', 'q', 'w', 'w'], 3))
# # print 6
# # one of the possible orders to run the task would be
# # 'q', 'w', 's', idle, 'q', 'w'
from collections import deque
from typing import Deque, Dict, List, Optional


def find_shortest_task_plan_with_cool_down_time_and_with_reordering(tasks: List[str], cool_down_time: int) -> List[
    Optional[str]]:
    occurrence_counts_by_tasks: Dict[str, int] = {}
    for task in tasks:
        if task in occurrence_counts_by_tasks:
            occurrence_counts_by_tasks[task] += 1
        else:
            occurrence_counts_by_tasks[task] = 1

    max_occurrence_count: int = 0
    task_list_by_occurrence_counts: Dict[int, List[str]] = {}
    for task in occurrence_counts_by_tasks.keys():
        occurrence_count: int = occurrence_counts_by_tasks[task]
        if occurrence_count in task_list_by_occurrence_counts:
            task_list_by_occurrence_counts[occurrence_count].append(task)
        else:
            task_list_by_occurrence_counts[occurrence_count] = [task]
        max_occurrence_count = max(max_occurrence_count, occurrence_count)

    last_occurrence_indices_by_tasks: Dict[str, int] = {}
    current_max_occurrence_count: int = max_occurrence_count
    schedule: List[Optional[str]] = []
    empty_slots: Deque[int] = deque()
    while len(task_list_by_occurrence_counts) > 0:
        new_max_occurrence_count: int = current_max_occurrence_count - 1
        if current_max_occurrence_count in task_list_by_occurrence_counts:
            tasks_with_current_occurrence_count: List[str] = task_list_by_occurrence_counts.pop(
                current_max_occurrence_count)
            for task in tasks_with_current_occurrence_count:

                if task not in last_occurrence_indices_by_tasks:
                    if len(empty_slots) > 0:
                        last_occurrence_indices_by_tasks[task] = empty_slots.popleft()
                    else:
                        last_occurrence_indices_by_tasks[task] = len(schedule)
                        # Will be overwritten by "task" right away.
                        schedule.append(None)

                elif task in last_occurrence_indices_by_tasks:
                    if len(empty_slots) > 0 and empty_slots[len(empty_slots) - 1] - last_occurrence_indices_by_tasks[
                        task] >= cool_down_time:
                        current_index: int = 0
                        while empty_slots[current_index] - last_occurrence_indices_by_tasks[task] < cool_down_time:
                            current_index += 1
                        last_occurrence_indices_by_tasks[task] = empty_slots[current_index]
                        empty_slots.__delitem__(current_index)

                    else:
                        while (len(schedule) - 1) - last_occurrence_indices_by_tasks[task] < cool_down_time:
                            empty_slots.append(len(schedule))
                            schedule.append(None)
                        last_occurrence_indices_by_tasks[task] = len(schedule)
                        # Will be overwritten by "task" right away.
                        schedule.append(None)

                schedule[last_occurrence_indices_by_tasks[task]] = task

                if new_max_occurrence_count > 0:
                    if new_max_occurrence_count in task_list_by_occurrence_counts:
                        task_list_by_occurrence_counts[new_max_occurrence_count].append(task)
                    else:
                        task_list_by_occurrence_counts[new_max_occurrence_count] = [task]

        current_max_occurrence_count = new_max_occurrence_count

    return schedule
