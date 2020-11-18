# Task:
#
# You are given a hash table where the key is a vertex V1 and the value is a list of all vertices (V2, V3, ...) that
# directed edges are going from that vertex to, i.e. V1->V2, V1->V3 etc. Find any cycle in the graph if there are any.
# Return NULL otherwise.
#
# Example 1:
# {
#   'V1': ['V3', 'V2'],
#   'V2': ['V3'],
#   'V3': []
# }
#
# This input should return NULL because there is no cycle:
#  NULL
#
# Example 2:
# {
#   'V1': ['V3', 'V2'],
#   'V2': ['V3'],
#   'V3': ['V1']
# }
#
# This input should return one of the cycles:
#  ['V1', 'V3'] or ['V1', 'V2', 'V3']
#
# Here's your starting point:
#
# def find_cycles(destinations_by_vertices_arg):
#   # Fill this in.
#
# destinations_by_vertices = {
#   'V1': ['V3', 'V2'],
#   'V2': ['V3'],
#   'V3': ['V1']
# }
# print find_cycle(destinations_by_vertices)
# # ['V1', 'V3'] or ['V1', 'V2', 'V3']
from typing import Dict, List, Set


def find_cycle_recursively_intern(vertex_to_process: str,
                                  processed_vertices: Set[str],
                                  vertices_in_cycle: List[str],
                                  destinations_by_vertices_arg: Dict[str, List[str]]):
    if vertex_to_process in vertices_in_cycle:
        return vertices_in_cycle
    elif vertex_to_process in processed_vertices:
        return None
    else:
        processed_vertices.add(vertex_to_process)
        vertices_in_cycle.append(vertex_to_process)
        for destination in destinations_by_vertices_arg[vertex_to_process]:
            result_cycle: List[str] = find_cycle_recursively_intern(destination, processed_vertices, vertices_in_cycle,
                                                                    destinations_by_vertices_arg)
            if result_cycle:
                return result_cycle
        vertices_in_cycle.remove(vertex_to_process)


# Uses the Depth First Search
# See https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
def find_cycle_recursively(destinations_by_vertices_arg: Dict[str, List[str]]):
    vertices_to_process = destinations_by_vertices_arg.keys()
    if len(vertices_to_process) == 0:
        return 'NULL'
    else:
        processed_vertices: Set[str] = set()

        for vertex in vertices_to_process:
            if vertex not in processed_vertices:
                result_cycle: List[str] = find_cycle_recursively_intern(vertex, processed_vertices, [],
                                                                        destinations_by_vertices_arg)
                if result_cycle:
                    return result_cycle
        return 'NULL'


destinations_by_vertices = {
    'V1': ['V3', 'V2'],
    'V2': ['V3'],
    'V3': ['V1']
}
print(find_cycle_recursively(destinations_by_vertices))
# ['V1', 'V3'] or ['V1', 'V2', 'V3']
destinations_by_vertices2 = {
    'V1': ['V2'],
    'V2': [],
    'V3': ['V4'],
    'V4': ['V5'],
    'V5': ['V2']
}
print(find_cycle_recursively(destinations_by_vertices2))
# NULL
destinations_by_vertices3 = {
    'V1': ['V1']
}
print(find_cycle_recursively(destinations_by_vertices3))
# ['V1']
