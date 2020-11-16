# Task:
#
# Given a nested dictionary, flatten the dictionary, where nested dictionary keys can be represented through dot
# notation.
#
# Example:
#
# Input: {
#   'a': 1,
#   'b': {
#     'c': 2,
#     'd': {
#       'e': 3
#     }
#   }
# }
# Output: {
#   'a': 1,
#   'b.c': 2,
#   'b.d.e': 3
# }
#
# You can assume there will be no arrays, and all keys will be strings.
#
# Here's some starter code:
#
# def flatten_dictionary(d):
#   # Fill this in.
#
# d = {
#     'a': 1,
#     'b': {
#         'c': 2,
#         'd': {
#             'e': 3
#         }
#     }
# }
# print(flatten_dictionary(d))
# # {'a': 1, 'b.c': 2, 'b.d.e': 3}
from collections import deque
from typing import Deque, Dict, Optional, Tuple


def flatten_dictionary(input_dictionary: Dict[str, object]) -> Dict[str, object]:
    dictionary_prefix: Deque[Tuple[Dict[str, object], Optional[str]]] = deque()
    dictionary_prefix.append((input_dictionary, None))

    result: Dict[str, object] = {}

    while len(dictionary_prefix) > 0:
        current_dictionary, prefix = dictionary_prefix.pop()
        for current_key in current_dictionary.keys():
            new_prefix: str = '{}.{}'.format(prefix, current_key) if prefix is not None else current_key
            current_value = current_dictionary[current_key]
            if isinstance(current_value, Dict):
                dictionary_prefix.append((current_value, new_prefix))
            else:
                result[new_prefix] = current_value
    return result


d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
