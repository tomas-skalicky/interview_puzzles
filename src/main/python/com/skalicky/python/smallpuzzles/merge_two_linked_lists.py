class ListNode(object):
    def __init__(self,
                 value,
                 name,
                 next_node=None):
        self.value = value
        self.name: str = name
        self.next_node: ListNode = next_node

    # Necessary for comparison in merge_* functions
    def __le__(self,
               other):
        return self.value <= other.value

    def __str__(self):
        return '{0}:{1}'.format(self.value, self.name)


def merge_iteratively(list1_node1: ListNode,
                      list2_node1: ListNode):
    result_list_node1: ListNode = ListNode(-1000, 'dummy')
    result_list_current_node: ListNode = result_list_node1
    current_list1_node: ListNode = list1_node1
    current_list2_node: ListNode = list2_node1
    while current_list1_node is not None or current_list2_node is not None:
        if current_list1_node is None:
            if current_list2_node is not None:
                result_list_current_node.next_node = current_list2_node
            break
        elif current_list2_node is None:
            result_list_current_node.next_node = current_list1_node
            break
        else:
            if current_list1_node <= current_list2_node:
                result_list_current_node.next_node = current_list1_node
                current_list1_node = current_list1_node.next_node
            else:
                result_list_current_node.next_node = current_list2_node
                current_list2_node = current_list2_node.next_node
            result_list_current_node = result_list_current_node.next_node
    return result_list_node1.next_node


def merge_recursively(list1_node1: ListNode,
                      list2_node1: ListNode):
    result_list_node1: ListNode = ListNode(-1000, 'dummy')
    merge_recursively_intern(result_list_node1, list1_node1, list2_node1)
    return result_list_node1.next_node


def merge_recursively_intern(result_list_current_node: ListNode,
                             current_list1_node: ListNode,
                             current_list2_node: ListNode):
    if current_list1_node is None:
        if current_list2_node is not None:
            result_list_current_node.next_node = current_list2_node
    elif current_list2_node is None:
        result_list_current_node.next_node = current_list1_node
    else:
        if current_list1_node <= current_list2_node:
            result_list_current_node.next_node = current_list1_node
            merge_recursively_intern(current_list1_node, current_list1_node.next_node, current_list2_node)
        else:
            result_list_current_node.next_node = current_list2_node
            merge_recursively_intern(current_list2_node, current_list1_node, current_list2_node.next_node)


def print_linked_list(list1_node1: ListNode):
    print()
    if list1_node1 is None:
        print('None')
    else:
        current_node = list1_node1
        while current_node is not None:
            print(current_node)
            current_node = current_node.next_node


def create_linked_lists():
    # Linked lists created reversibly
    list1_node5 = ListNode(20, 'list1_node5')
    list1_node4 = ListNode(18, 'list1_node4', list1_node5)
    list1_node3 = ListNode(8, 'list1_node3', list1_node4)
    list1_node2 = ListNode(3, 'list1_node2', list1_node3)
    list1_node1 = ListNode(1, 'list1_node1', list1_node2)

    list2_node4 = ListNode(7, 'list2_node4')
    list2_node3 = ListNode(6, 'list2_node3', list2_node4)
    list2_node2 = ListNode(3, 'list2_node2', list2_node3)
    list2_node1 = ListNode(2, 'list2_node1', list2_node2)

    return list1_node1, list2_node1


# Task: Given two sorted linked lists, merge them in order.
def main():
    list1_node1, list2_node1 = create_linked_lists()

    merged_list_from_iterative_approach_node1: ListNode = merge_iteratively(list1_node1, list2_node1)
    print_linked_list(merged_list_from_iterative_approach_node1)

    empty_merged_list_from_iterative_approach_node1: ListNode = merge_iteratively(None, None)
    print_linked_list(empty_merged_list_from_iterative_approach_node1)

    list3_node1, list4_node2 = create_linked_lists()

    merged_list_from_recursive_approach_node1: ListNode = merge_recursively(list3_node1, list4_node2)
    print_linked_list(merged_list_from_recursive_approach_node1)

    empty_merged_list_from_recursive_approach_node1: ListNode = merge_iteratively(None, None)
    print_linked_list(empty_merged_list_from_recursive_approach_node1)


main()
