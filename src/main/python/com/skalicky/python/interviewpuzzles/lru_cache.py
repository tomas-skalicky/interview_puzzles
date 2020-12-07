# Task:
#
# LRU cache is a cache data structure that has limited space, and once there are more items in the cache than available
# space, it will preempt the least recently used item. What counts as recently used is any item a key has 'get' or 'put'
# called on it.
#
# Implement an LRU cache class with the 2 functions 'put' and 'get'. 'put' should place a value mapped to a certain key,
# and preempt items if needed. 'get' should return the value for a given key if it exists in the cache, and return None
# if it doesn't exist.
#
# Here's some examples and some starter code.
#
# class LruCache:
#     def __init__(self, capacity):
#         # Fill this in.
#
#     def get(self, key):
#         # Fill this in.
#
#     def put(self, key, value):
#         # Fill this in.
#
# cache = LRUCache(2)
#
# cache.put(3, 3)
# cache.put(4, 4)
# print(cache.get(3))
# # 3
# print(cache.get(2))
# # None
#
# cache.put(2, 2)
#
# print(cache.get(4))
# # None (pre-empted by 2)
# print(cache.get(3))
# # 3
from typing import Dict, Optional, Tuple


class KeyNode:
    def __init__(self, key):
        self.key = key
        self.next_node: Optional[KeyNode] = None
        self.previous_node: Optional[KeyNode] = None

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node
        if new_next_node is not None:
            new_next_node.previous_node = self

    def __repr__(self) -> str:
        return '{} -> {}'.format(self.key, self.next_node)


class LruCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.head_node: Optional[KeyNode] = None
        self.tail_node: Optional[KeyNode] = None
        self.map: Dict[object, object] = {}

    def __repr__(self) -> str:
        return 'capacity={}, linked list starting with head=({}), linked list starting with tail=({})'.format(
            self.capacity, self.head_node, self.tail_node)

    def search(self, key) -> Tuple[Optional[KeyNode], Optional[KeyNode]]:
        previous_node: Optional[KeyNode] = None
        current_node: KeyNode = self.head_node
        while current_node is not None and current_node.key != key:
            previous_node = current_node
            current_node = current_node.next_node
        return current_node, previous_node

    def get(self, key) -> Optional[object]:
        """Time complexity ... if the key is not in the cache, then O(1). If the key is in the cache, then O(n) in the
        worst case.
        """
        if key not in self.map:
            return None
        else:
            current_node, previous_node = self.search(key)
            if previous_node is None:
                # Nothing to do because the head node is already the most recently used node.
                pass
            else:
                if self.tail_node == current_node:
                    self.tail_node = previous_node
                previous_node.set_next_node(current_node.next_node)
                current_node.set_next_node(self.head_node)
                self.head_node = current_node
            return self.map[key]

    def put(self, key, value):
        """Time complexity ... if the key is not in the cache, then O(1). If the key is in the cache, then O(n) in the
        worst case.
        """
        if key not in self.map:
            if self.capacity == 0:
                return
            else:
                if len(self.map.keys()) == self.capacity:
                    self.map.pop(self.tail_node.key)
                    if self.capacity == 1:
                        self.head_node = None
                        self.tail_node = None
                    else:
                        # Last node removed
                        self.tail_node = self.tail_node.previous_node
                        self.tail_node.next_node = None

                new_node: KeyNode = KeyNode(key)
                new_node.set_next_node(self.head_node)
                self.head_node = new_node
                if self.tail_node is None:
                    self.tail_node = self.head_node

        else:
            # Moves in the head.
            self.get(key)

        self.map[key] = value
