# Task:
#
# You are given a hash table where the key is a course code, and the value is a list of all the course codes that are
# prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists,
# return NULL.
#
# Example:
# {
#   'CSC300': ['CSC100', 'CSC200'],
#   'CSC200': ['CSC100'],
#   'CSC100': []
# }
#
# This input should return the order that we need to take these courses:
#  ['CSC100', 'CSC200', 'CSCS300']
#
# Here's your starting point:
#
# def courses_to_take(course_to_prereqs):
#   # Fill this in.
#
# courses = {
#   'CSC300': ['CSC100', 'CSC200'],
#   'CSC200': ['CSC100'],
#   'CSC100': []
# }
# print courses_to_take(courses)
# # ['CSC100', 'CSC200', 'CSC300']
from typing import Dict, List, Set


def create_courses_to_take_dictionary(course_to_prereqs: Dict[str, List[str]]):
    successors_by_courses: Dict[str, Set[str]] = {}
    for course in course_to_prereqs.keys():
        successors_by_courses[course] = set()
    for course in course_to_prereqs.keys():
        for prereq in course_to_prereqs[course]:
            successors_by_courses[prereq].add(course)
    return successors_by_courses


def sort_courses_by_prereq_count_by_radix(course_to_prereqs: Dict[str, List[str]]):
    courses_and_prereq_counts: List[Set[str]] = [set()]
    for course in course_to_prereqs:
        prereq_count = len(course_to_prereqs[course])
        while len(courses_and_prereq_counts) <= prereq_count:
            courses_and_prereq_counts.append(set())
        courses_and_prereq_counts[prereq_count].add(course)
    return courses_and_prereq_counts


def courses_to_take(course_to_prereqs: Dict[str, List[str]]):
    successors_by_courses: Dict[str, Set[str]] = create_courses_to_take_dictionary(course_to_prereqs)
    courses_sorted_by_prereq_count_by_radix = sort_courses_by_prereq_count_by_radix(course_to_prereqs)
    result_ordering: List[str] = []
    while len(successors_by_courses.keys()) > 0 and len(courses_sorted_by_prereq_count_by_radix[0]) > 0:
        course_to_process: str = courses_sorted_by_prereq_count_by_radix[0].pop()
        result_ordering.append(course_to_process)

        successors: Set[str] = successors_by_courses.pop(course_to_process)
        for successor in successors:
            successor_prereq: List[str] = course_to_prereqs.get(successor)
            successor_old_count: int = len(successor_prereq)
            successor_prereq.remove(course_to_process)
            successor_new_count: int = len(successor_prereq)
            courses_sorted_by_prereq_count_by_radix[successor_old_count].remove(successor)
            courses_sorted_by_prereq_count_by_radix[successor_new_count].add(successor)

    if len(successors_by_courses.keys()) > 0:
        return 'NULL'
    else:
        return result_ordering


courses = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
courses2 = {
    'CSC500': ['CSC400'],
    'CSC400': [],
    'CSC300': ['CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': ['CSC400']
}
print(courses_to_take(courses2))
# ['CSC400', 'CSC100', 'CSC500', 'CSC200', 'CSC300']
# or
# ['CSC400', 'CSC500', 'CSC100', 'CSC200', 'CSC300']
courses3 = {
    'CSC300': ['CSC300']
}
print(courses_to_take(courses3))
# NULL
courses4 = {
    'CSC500': ['CSC400'],
    'CSC400': [],
    'CSC300': ['CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': ['CSC300']
}
print(courses_to_take(courses4))
# NULL
courses5 = {}
print(courses_to_take(courses5))
# []
