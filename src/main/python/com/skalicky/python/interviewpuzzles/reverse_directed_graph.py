# Task:
#
# Given a directed graph, reverse the directed graph so all directed edges are reversed.
#
# Example:
# Input:
# A -> B, B -> C, A ->C
#
# Output:
# B->A, C -> B, C -> A
# Here's a starting point:
#
# from collections import defaultdict
#
# class Node:
#   def __init__(self, value):
#     self.adjacent = []
#     self.value = value
#
# def reverse_graph(graph):
#   # Fill this in.
#
# a = Node('a')
# b = Node('b')
# c = Node('c')
#
# a.adjacent += [b, c]
# b.adjacent += [c]
#
# graph = {
#     a.value: a,
#     b.value: b,
#     c.value: c,
# }
#
# for _, val in reverse_graph(graph).items():
#   print(val.adjacent)
# # []
# # ['a', 'b']
# # ['a']


from typing import Dict, List


class Node:
    def __init__(self, value: object):
        self.adjacent: List[Node] = []
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


def reverse_graph(graph_input: Dict[object, Node]) -> Dict[object, Node]:
    reversed_graph: Dict[object, Node] = dict()
    for current_node_value in graph_input.keys():
        reversed_graph[current_node_value] = Node(current_node_value)
    for current_node_value in graph_input.keys():
        current_node: Node = graph_input[current_node_value]
        for current_adjacent in current_node.adjacent:
            reversed_graph[current_adjacent.value].adjacent.append(current_node)
    return reversed_graph


a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

result_reversed_graph: Dict[object, Node] = reverse_graph(graph)
for node_value in result_reversed_graph.keys():
    for adjacent in result_reversed_graph[node_value].adjacent:
        print('{} -> {}'.format(node_value, adjacent))
# b -> a
# c -> a
# c -> b
